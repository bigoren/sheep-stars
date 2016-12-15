import socket
import array
import time
import random
import msvcrt
import win32api
import win32con
import random
import time, wave, pymedia.audio.sound as sound
import os.path
import json

import star
import leds_effects
import single_star_effect
import effect_stars_swipe
import effect_stars_group_random
import config_leds

start_time = time.time()
cicle_number = 0

#network
CONTROLER_IP = "192.168.1.210"
UDP_PORT = 2000
sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

						
#sound
f = wave.open(r'C:\Users\Amir\Downloads\dreams.wav', 'rb')
sampleRate= f.getframerate()
sound_frames_per_cicle = int(sampleRate / config_leds.frames_per_second)
channels= f.getnchannels()
format= sound.AFMT_S16_LE
snd= sound.Output( sampleRate, channels, format )
	
def parse_json_effect(json_str):
	json_obj = json.loads(json_str)
	effect_name = json_obj["effect_name"]
	params = json_obj["parameters"]
	
	eff = None
	if effect_name == "SingleStar":
		eff = single_star_effect.SingleStarEffect()
	elif effect_name == "StarsSwipe":
		eff = effect_stars_swipe.SingleStarEffect()
	elif effect_name == "StarsGroupRandom":
		eff = effect_stars_group_random.EffectStarsGroupRandom()
	if eff:
		eff.from_json(params)
		
	return eff
		
starts_swipe_effect = None

		

def fade_to_black():
	for i in range(len(base_pattern)):
		base_pattern[i] = int(base_pattern[i] * 0.9)

def set_pixel(index, color):
	for channel in range(0,3):
		base_pattern[index * 3 + channel] = color[channel]
		
def is_pixel_off(index):
	for channel in range(3):
		if base_pattern[index * 3 + channel] != 0:
			return False
	return True

def get_color(pixel):
	return [255, 0, 0]
		
print dir(config_leds)
if os.path.isfile(config_leds.current_file):
	effects = {}
	leds_f = open(config_leds.current_file, "r")
	effects = [parse_json_effect(l) for l in leds_f.readlines()]
	
	while True:
		s = f.readframes( sound_frames_per_cicle )
		snd.play( s )
		
		for effect in effects:
			effect.apply(cicle_number)
		for s in star.stars:
			s.draw(cicle_number)
		header = array.array('B', [0, 0, 0, 0])
		pixels_data = array.array('B', star.stars_buf)
		message_on_net = (header + pixels_data).tostring()
		print len(message_on_net)
		cicle_number = cicle_number + 1
		next_frame_time = start_time + (cicle_number / config_leds.frames_per_second)
		leds_frame_in_audio = cicle_number * sound_frames_per_cicle
		while f.tell() < leds_frame_in_audio: 
			time.sleep(0.001)
		sock.sendto(message_on_net, (CONTROLER_IP, UDP_PORT))

"""
else:		
	leds_f = open(fname, "w")
	kdf = None #key down frame
	sssf = None
	grsf = None
	e = None
	egr = []
		
	while True:

		s = f.readframes( sound_frames_per_cicle )
		snd.play( s )
		
		k1 = win32api.GetAsyncKeyState(win32con.VK_NUMPAD1) 
		k2 = win32api.GetAsyncKeyState(win32con.VK_NUMPAD2) 
		k3 = win32api.GetAsyncKeyState(win32con.VK_NUMPAD3) 
		k4 = win32api.GetAsyncKeyState(win32con.VK_NUMPAD4) 
		
		if cicle_number % 1 == 0:
			pass
			#fade_to_black()

		if k3 and not grsf:
			grsf = cicle_number
			new_effect = effect_stars_group_random.EffectStarsGroupRandom()
			new_effect.set_parameters(cicle_number, 50, 50, 50, 5)
			egr.append(new_effect)
		elif not k3 and grsf is not None:
			new_effect = effect_stars_group_random.EffectStarsGroupRandom()
			new_effect.set_parameters(grsf, 50, max(cicle_number - grsf - 100, 0), 50, 5)
			leds_f.write(new_effect.to_json() + '\n')
			grsf = None
			
		for egr_e in egr:
			egr_e.apply(cicle_number)
			
		if k2 and not sssf:
			sssf = cicle_number
			e = effect_stars_swipe.SingleStarEffect()
			e.set_parameters(cicle_number, cicle_number + 300)
		elif not k2 and sssf:
			new_effect = effect_stars_swipe.SingleStarEffect()
			new_effect.set_parameters(sssf, cicle_number)
			leds_f.write(new_effect.to_json() + '\n')
			sssf = None
			
		if e:
			is_on = e.apply(cicle_number)
			if not is_on:
				e = None
		
		if k1 and kdf is None:
			r = random.randint(0, 50-1)
			star.stars[r].set_parameters(cicle_number, 10, 50, 30, [255, 255, 255])
			kdf = cicle_number
		elif not k1 and kdf is not None:
			index = random.randint(0, 50-1)
			on_end_frame = cicle_number - 30
			on_frames = max(0, on_end_frame - kdf)
			new_effect = single_star_effect.SingleStarEffect()
			new_effect.set_parameters(index, kdf - 10, 10, on_frames, 30)
			leds_f.write(new_effect.to_json() + '\n')
			kdf = None
				
		for s in star.stars:
			s.draw(cicle_number)
			
		message_on_net = array.array('B', star.stars_buf).tostring()
		cicle_number = cicle_number + 1
		next_frame_time = start_time + (cicle_number / config_leds.frames_per_second)
		leds_frame_in_audio = cicle_number * sound_frames_per_cicle
		while f.tell() < leds_frame_in_audio: 
			time.sleep(0.001)
		sock.sendto(message_on_net, (CONTROLER_IP, UDP_PORT))
						
"""













	
	