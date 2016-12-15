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

import config_leds
import effect_stars_group_random

start_time = time.time()
cicle_number = 0

#sound
f = wave.open(r'C:\Users\Amir\Downloads\dreams.wav', 'rb')

orig_sample_rate= f.getframerate()
slow_factor = 1

sound_frames_per_cicle = int(orig_sample_rate / config_leds.frames_per_second)
channels= f.getnchannels()
format= sound.AFMT_S16_LE
snd= sound.Output( int(orig_sample_rate * slow_factor), channels, format )
	
fname = r"c:\tmp\1.json"

leds_f = open(fname, "a")

key_down = False

while True:

	s = f.readframes(sound_frames_per_cicle)
	snd.play( s )
	
	k1 = win32api.GetAsyncKeyState(win32con.VK_NUMPAD1) 
	k2 = win32api.GetAsyncKeyState(win32con.VK_NUMPAD2) 
	k3 = win32api.GetAsyncKeyState(win32con.VK_NUMPAD3) 
	k4 = win32api.GetAsyncKeyState(win32con.VK_NUMPAD4) 
	
	if k1 and key_down is False:
		print cicle_number
		key_down = True
		new_effect = effect_stars_group_random.EffectStarsGroupRandom()
		new_effect.set_parameters(cicle_number, 50, random.randint(30,70), 50, random.randint(2,10))
		leds_f.write(new_effect.to_json() + '\n')
	elif not k1 and key_down is True:
		key_down = False
		
	cicle_number = cicle_number + 1
	leds_frame_in_audio = cicle_number * sound_frames_per_cicle
	while f.tell() < leds_frame_in_audio: 
		time.sleep(0.001)
						














	
	