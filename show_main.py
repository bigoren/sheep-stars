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

#network
UDP_IP_1234 = "192.168.2.201"
UDP_PORT = 2000
sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

#leds
num_pixels = 150
pixel_array_size = num_pixels * 3
base_pattern = [0] * pixel_array_size
frames_per_second = 50.0
start_time = time.time()
cicle_number = 0
						
#sound
f = wave.open(r'C:\Users\Bigi\Documents\Arduino\Aerosmith_Dream_On.wav', 'rb')
sampleRate= f.getframerate()
sound_frames_per_cicle = int(sampleRate / frames_per_second)
channels= f.getnchannels()
format= sound.AFMT_S16_LE
snd= sound.Output( sampleRate, channels, format )


class Star:
	
	self._begin_frame = None
	self._start_frames = None
	self._on_frames = None
	self._end_frames = None
	
	def __init__(self, index_on_arr):
		self._index_on_arr = index_on_arr
	
	def set_parameters(self, curr_frame, start_frames, on_frames, end_frames):
		
		if self._start_frames is None: # the star is currently OFF
			self._begin_frame = curr_frame
			self._start_frames = start_frames
			self._on_frames = on_frames
			self._end_frames = end_frames
			
		else: # star is currently ON, need to merge
			
			
	def draw(self):
		pass
	

class LedsEffect:
	
	def to_json(self):
		return json.dumps({"effect_name" : self.get_name(), "parameters" : self.params_as_dict() })
		
	def from_json(self, params):
		self.params_from_dict(params)		
	
class StarsSwipe(LedsEffect):

	def get_name(self):
		return "StarsSwipe"

	def __init__(self):
		self._width_frames = 10
		
	def set_start_frame(self, cycle_number):
		self._start_frame = cycle_number
	def set_end_frame(self, cycle_number):
		self._end_frame = cycle_number
		
	def params_as_dict(self):
		return {"start_frame" : self._start_frame, "end_frame" : self._end_frame}
		
	def params_from_dict(self, params):
		self._start_frame = int(params["start_frame"])
		self._end_frame = int(params["end_frame"])
		
	def apply(self, curr_frame):
		if curr_frame >= self._end_frame or curr_frame < self._start_frame:
			return
		rel_pos = (curr_frame - self._start_frame) / float( (self._end_frame - self._width_frames) - self._start_frame)
		pos = int(rel_pos * num_pixels)
		if pos >= 0 and pos < num_pixels and is_pixel_off(pos) and random.randint(0,4) == 0:
			rand_intensity = random.randint(0,255 - 1)
			set_pixel(pos, [rand_intensity, rand_intensity, rand_intensity])
		fade_to_black()

def parse_json_effect(json_str):
	json_obj = json.loads(json_str)
	effect_name = json_obj["effect_name"]
	params = json_obj["parameters"]
	
	eff = None
	if effect_name == "StarsSwipe":
		eff = StarsSwipe()
	
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
		
fname = r"c:\temp\1234_sound.txt"
if os.path.isfile(fname):
	effects = {}
	leds_f = open(fname, "r")
	effects = [parse_json_effect(l) for l in leds_f.readlines()]
	
	while True:
		s = f.readframes( sound_frames_per_cicle )
		snd.play( s )
		
		'''
		if cicle_number in commands:
			is_on = commands[cicle_number]
			print cicle_number
			
		if cicle_number % 3 == 0:
			fade_to_black()
		if is_on:
			for _ in range(3):
				r = random.randint(0,299)
				set_pixel(r, get_color(r))	
		'''
		
		for effect in effects:
			effect.apply(cicle_number)
		message_window = array.array('B', base_pattern).tostring()
		cicle_number = cicle_number + 1
		next_frame_time = start_time + (cicle_number / frames_per_second)
		leds_frame_in_audio = cicle_number * sound_frames_per_cicle
		while f.tell() < leds_frame_in_audio: 
			time.sleep(0.001)
		sock.sendto(message_window, (UDP_IP_1234, UDP_PORT))
		
else:		
	leds_f = open(fname, "w")
	is_on = False
		
	while True:

		s = f.readframes( sound_frames_per_cicle )
		snd.play( s )
			
		k1 = win32api.GetAsyncKeyState(win32con.VK_NUMPAD1) 
		k2 = win32api.GetAsyncKeyState(win32con.VK_NUMPAD2) 
		k3 = win32api.GetAsyncKeyState(win32con.VK_NUMPAD3) 
		k4 = win32api.GetAsyncKeyState(win32con.VK_NUMPAD4) 
		
		if k1 and not starts_swipe_effect:
			starts_swipe_effect = StarsSwipe()
			starts_swipe_effect.set_start_frame(cicle_number)
		elif not k1 and starts_swipe_effect:
			starts_swipe_effect.set_end_frame(cicle_number)
			leds_f.write(starts_swipe_effect.to_json() + '\n')
			starts_swipe_effect = None

		if cicle_number % 1 == 0:
			fade_to_black()
		
		if is_on:
			for _ in range(5):
				r = random.randint(0,num_pixels-1)
				set_pixel(r, get_color(r))
			
		message_window = array.array('B', base_pattern).tostring()
		cicle_number = cicle_number + 1
		next_frame_time = start_time + (cicle_number / frames_per_second)
		leds_frame_in_audio = cicle_number * sound_frames_per_cicle
		while f.tell() < leds_frame_in_audio: 
			time.sleep(0.001)
		sock.sendto(message_window, (UDP_IP_1234, UDP_PORT))
						














	
	