
import time, wave, pymedia.audio.sound as sound

import sheep
import networking
import config_leds

import sheep_shine_effect

start_time = time.time()

e = sheep_shine_effect.SheepShineEffect()
e.set_parameters(1, 0, 100, 100, 100)

#sound
f = wave.open(r'C:\Users\Amir\Downloads\dreams.wav', 'rb')
sampleRate= f.getframerate()
sound_frames_per_cicle = int(sampleRate / config_leds.frames_per_second)
channels= f.getnchannels()
format= sound.AFMT_S16_LE
snd= sound.Output( int(sampleRate), channels, format )

for cicle_number in range(0, 1000):

	s = f.readframes( sound_frames_per_cicle )
	snd.play( s )
	
	e.apply(cicle_number)
		
	next_frame_time = start_time + (cicle_number / config_leds.frames_per_second)
	leds_frame_in_audio = cicle_number * sound_frames_per_cicle
	while f.tell() < leds_frame_in_audio: 
		time.sleep(0.001)
	networking.send(cicle_number)

	
"""
sheep.sheep_1.set_head([ [0,255,0] ] * sheep.sheep_1.head_len)
sheep.sheep_1.set_l_ear([ [255,0,0] ] * sheep.sheep_1.l_ear_len)
sheep.sheep_1.set_r_ear([ [255,0,0] ] * sheep.sheep_1.r_ear_len)
sheep.sheep_1.set_ll_leg([ [0,0,255] ] * sheep.sheep_1.ll_leg_len)
sheep.sheep_1.set_lr_leg([ [0,0,255] ] * sheep.sheep_1.lr_leg_len)
sheep.sheep_1.set_rl_leg([ [0,0,255] ] * sheep.sheep_1.rl_leg_len)
sheep.sheep_1.set_rr_leg([ [0,0,255] ] * sheep.sheep_1.rr_leg_len)
sheep.sheep_1.set_body([ [255,0,255] ] * sheep.sheep_1.body_len)
"""

