import socket
import array
import time
import random
#import msvcrt
#import win32api
#import win32con
import random
#import time, wave, pymedia.audio.sound as sound
import os.path
import json

import star
import leds_effects
import single_star_effect
import effect_stars_swipe
import effect_stars_group_random
import config_leds
from UIElements.SmallSheep import SmallSheep
from Animations_Sheep.BlinkCircleAnimation import BlinkCircleAnimation

start_time = time.time()
circle_number = 0

#network
CONTROLER_IP = "192.168.2.210" #"192.168.1.210"
UDP_PORT = 2000
sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

#sound
#f = wave.open(r'C:\Users\Amir\Downloads\dreams.wav', 'rb')
#sampleRate= f.getframerate()
#sound_frames_per_cicle = int(sampleRate / config_leds.frames_per_second)
#channels= f.getnchannels()n
#format= sound.AFMT_S16_LE
#snd= sound.Output( sampleRate, channels, format )

#sheep (Red, Green, Blue)
#star (Green, Red, Blue )

print "hey"

smallSheep = SmallSheep()
animation = BlinkCircleAnimation(smallSheep, 500, [200, 128, 150])

while True:
    

	
    header = array.array('B', [0, (circle_number / (256 * 256) ) % 256, (circle_number / 256) % 256, circle_number % 256])
    message_0 = (header + array.array('B', [0] * 900)).tostring()
    
    header = array.array('B', [1, (circle_number / (256 * 256) ) % 256, (circle_number / 256) % 256, circle_number % 256])
    message_1 = (header + array.array('B', [0] * 900)).tostring()
                
    header = array.array('B', [2, (circle_number / (256 * 256) ) % 256, (circle_number / 256) % 256, circle_number % 256])
    message_2 = (header + array.array('B', [0] * 900)).tostring()

    header = array.array('B', [0, (circle_number / (256 * 256) ) % 256, (circle_number / 256) % 256, circle_number % 256])
    smallSheepArr = [1,1,1] * 300
    animation.apply(circle_number, smallSheepArr)
    pixels_data = array.array('B', smallSheepArr)
    message_3 = (header + pixels_data).tostring()

    header = array.array('B', [4, (circle_number / (256 * 256) ) % 256, (circle_number / 256) % 256, circle_number % 256])
    message_4 = (header + array.array('B', [0] * 900)).tostring()
                
    circle_number = circle_number + 1

    #sock.sendto(message_0, (CONTROLER_IP, UDP_PORT))
    sock.sendto(message_1, (CONTROLER_IP, UDP_PORT))
    #sock.sendto(message_2, (CONTROLER_IP, UDP_PORT))
    sock.sendto(message_3, (CONTROLER_IP, UDP_PORT))
    #sock.sendto(message_4, (CONTROLER_IP, UDP_PORT))

    time.sleep(0.001)
	













	
	
