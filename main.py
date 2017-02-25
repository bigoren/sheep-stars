#import RPi.GPIO as GPIO
from time import sleep
import pygame
from Song.Dreams import Dreams
from Song.FroggyWoogie import FroggyWoogie
from Song.ChronosThought import ChronosThought
from Song.CloudstructureLasttime import CloudstructureLasttime
from Song.TaPaDa import TaPaDa
from Song.Borealis import Borealis
from Song.SweetDreams import SweetDreams
from Song.DreamOn import DreamOn
from Song.ChristmasDubstep import ChristmasDubstep
from Song.NiceDream import NiceDream
import networking_may as networking
import random
import colorsys

from UIElements.SmallSheep import SmallSheep
from UIElements.BigSheep12 import BigSheep12
from UIElements.BigSheep34 import BigSheep34
from UIElements.Signs import Signs
from UIElements.Flower import Flower

########################################################
# setup GPIO
########################################################

#GPIO.cleanup()
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.IN, GPIO.PUD_DOWN)
#GPIO.setup(22, GPIO.IN, GPIO.PUD_DOWN)
#GPIO.setup(4, GPIO.OUT)
#GPIO.setup(27, GPIO.OUT)

########################################################
# button defs
########################################################

def lit_button1():
#    GPIO.output(4, GPIO.HIGH)
    return
    
def lit_button2():
#    GPIO.output(27, GPIO.HIGH)
    return
    
def unlit_button1():
#    GPIO.output(4, GPIO.LOW)
    return

def unlit_button2():    
#    GPIO.output(27, GPIO.LOW)
    return

def button1_is():
#    return GPIO.input(17)
    return

def button2_is():
#    return GPIO.input(22)
    return

def send_signs(on1, on2, color):
    data1 = [0,0,0] * 75
    data2 = [0,0,0] * 75
    if (on1):
        data1 = color *75
    if (on2):
        data2 = color *75
    networking.sendSigns(0, data1+data2)
    
def animate_sheeps_sound(trans_cycles):
    smallSheep = SmallSheep()
    smallSheepArr = [0] * len(smallSheep.get_array())
    for i in range(len(smallSheep.get_all_indexes())):
        smallSheepArr[smallSheep.get_all_indexes()[i]*3 : smallSheep.get_all_indexes()[i]*3+3] = [5,5,5]
    smallSheepArr[900 : 906] = [255,0,0,255,0,0]
    bigSheep12 = BigSheep12()
    bigSheep12Arr = [0] * len(bigSheep12.get_array())
    for i in range(len(bigSheep12.get_all_indexes())):
        bigSheep12Arr[bigSheep12.get_all_indexes()[i]*3 : bigSheep12.get_all_indexes()[i]*3+3] = [5,5,5]
    bigSheep34 = BigSheep34()
    bigSheep34Arr = [0] * len(bigSheep34.get_array())
    for i in range(len(bigSheep34.get_all_indexes())):
        bigSheep34Arr[bigSheep34.get_all_indexes()[i]*3 : bigSheep34.get_all_indexes()[i]*3+3] = [5,5,5]
    
    signs = Signs()
    signsArr = [0] * len(signs.get_array())
    for i in range(len(signs.get_all_indexes())):
        signsArr[signs.get_all_indexes()[i]*3 : signs.get_all_indexes()[i]*3+3] = [5,5,5]

    flower = Flower()
    flowerArr = [0] * len(flower.get_array())
    for i in range(len(flower.get_all_indexes())):
        flowerArr[flower.get_all_indexes()[i]*3 : flower.get_all_indexes()[i]*3+3] = [10,0,0]
    for i in range(len(flower.get_seeds())):
        flowerArr[flower.get_seeds()[i]*3 : flower.get_seeds()[i]*3+3] = [15,15,0]

    networking.send(trans_cycles,smallSheepArr,bigSheep12Arr,bigSheep34Arr,signsArr,flowerArr)

def transition(cycle_time=0.5,trans_cycles=60):
    print "buttons are on waiting for press"
    flag = 1
    pygame.mixer.init()
    pygame.mixer.music.load('Music/sheep.mp3')
    pygame.mixer.music.play()
    
    while (trans_cycles != 0):
        trans_cycles = trans_cycles - 1
        animate_sheeps_sound(trans_cycles)
        if flag:
            #print "light button"
            lit_button1()
            lit_button2()
            flag = 0
        else:
            #print "unlight button"
            unlit_button1()
            unlit_button2()
            flag = 1
        
        if button1_is():
            print "button 1 pushed! "
            unlit_button1()
        if button2_is():    
            print "button 2 pushed! "
            unlit_button2()
        if (button1_is() and button2_is()):
            print "Double PUSH!"
            unlit_button1()
            unlit_button2()
            pygame.mixer.stop()
            return 1
        sleep(cycle_time)
    return 0
        
def clap():
    pygame.mixer.init()
    pygame.mixer.music.load('Music/clap.mp3')
    pygame.mixer.music.play(0)
    clock = pygame.time.Clock()
    on1 = random.randrange(2)
    color = [int(c*255) for c in colorsys.hsv_to_rgb(random.random(), 0.75, 0.1)]
    while pygame.mixer.music.get_busy():
        clock.tick(50)
        send_signs(on1 == 0, on1 == 1, color)

def sheep():
    pygame.mixer.init()
    pygame.mixer.music.load('Music/sheep.mp3')
    pygame.mixer.music.play(0)
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(50)
        
def run(sleep_time=0.5,trans_cycles=60):
    while 1:

        song = ChristmasDubstep()
        song.play()
        user_answer=transition(sleep_time,trans_cycles)

        song = DreamOn()
        song.play()
        user_answer=transition(sleep_time,trans_cycles)

        song = FroggyWoogie()
        song.play()
        user_answer=transition(sleep_time,trans_cycles)

        song = SweetDreams()
        song.play()
        user_answer=transition(sleep_time,trans_cycles)
    
        
########################################################
# start the app
########################################################
##  run(sleep_time=0.5,trans_cycles=60)
##  make sure sleep_time*trans_cycles is about 30 to match transition sheep
run(0.3,30)

