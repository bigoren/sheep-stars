import RPi.GPIO as GPIO
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

########################################################
# setup GPIO
########################################################

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

########################################################
# button defs
########################################################

def lit_button1():
    GPIO.output(4, GPIO.HIGH)
def lit_button2():
    GPIO.output(27, GPIO.HIGH)

def unlit_button1():
    GPIO.output(4, GPIO.LOW)
def unlit_button2():    
    GPIO.output(27, GPIO.LOW)

def button1_is():
    return GPIO.input(17)

def button2_is():
    return GPIO.input(22)

def transition(cycle_time=0.5,trans_cycles=60):
    print "buttons are on waiting for press"
    flag = 1
    pygame.mixer.init()
    pygame.mixer.music.load('Music/sheep.mp3')
    pygame.mixer.music.play()
    
    while (trans_cycles != 0):
        trans_cycles = trans_cycles - 1
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
    while pygame.mixer.music.get_busy():
        clock.tick(50)

def sheep():
    pygame.mixer.init()
    pygame.mixer.music.load('Music/sheep.mp3')
    pygame.mixer.music.play(0)
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(50)
        
def run(sleep_time=0.5,trans_cycles=60):
    while 1:
        song = Dreams()
        #song.play()
        user_answer=transition(sleep_time)
        if (~user_answer):
            user_answer=transition(sleep_time)
        if (user_answer):
            clap()
            song = SweetDreams()
            song.play()
        song = FroggyWoogie()
        song.play()
        user_answer=transition(sleep_time)
        if (~user_answer):
            user_answer=transition(sleep_time)
        if (user_answer):
            clap()
            song = DreamOn()
            song.play()
        song = ChronosThought()
        song.play()
        user_answer=transition(sleep_time)
        if (~user_answer):
            user_answer=transition(sleep_time)
        if (user_answer):
            clap()
            song = ChristmasDubstep()
            song.play()
        song = CloudstructureLasttime()
        song.play()
        user_answer=transition(sleep_time)
        if (~user_answer):
            user_answer=transition(sleep_time)
        if (user_answer):
            clap()
            song = SweetDreams()
            song.play()
        song = TaPaDa()
        song.play()
        user_answer=transition(sleep_time)
        if (~user_answer):
            user_answer=transition(sleep_time)
        if (user_answer):
            clap()
            song = DreamOn()
            song.play()
        song = Borealis()
        song.play()
        user_answer=transition(sleep_time)
        if (~user_answer):
            user_answer=transition(sleep_time)
        if (user_answer):
            clap()
            song = ChristmasDubStep()
            song.play()
        song = SweetDreams()
        song.play()
        song = DreamOn()
        song.play()
        song = ChristmasDubStep()
        song.play()

        
########################################################
# start the app
########################################################
##  run(sleep_time=0.5,trans_cycles=60)
##  make sure sleep_time*trans_cycles is about 30 to match transition sheep
run(0.3,90)

