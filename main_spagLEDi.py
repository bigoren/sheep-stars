import RPi.GPIO as GPIO
from time import sleep
import networking_may as networking
import random
import math

from Colors import Colors

from UIElements.SmallSheep import SmallSheep
from UIElements.BigSheep12 import BigSheep12
from UIElements.BigSheep34 import BigSheep34

from Animations_Sheep.SpinningHeadAnimation import SpinningHeadAnimation
from Animations_Sheep.SheepConfettiAnimation import SheepConfettiAnimation
from Animations_Sheep.RainbowAnimation import RainbowAnimation
from Animations_Sheep.FadeInOutAnimation import FadeInOutAnimation
from Animations_Sheep.AlternateAnimation import AlternateAnimation
from Animations_Sheep.SnakeAnimation import SnakeAnimation
from Animations_Sheep.FibonacciAnimation import FibonacciAnimation
from Animations_Sheep.BrokenAnimation import BrokenAnimation


########################################################
# consts & current loop data
########################################################

FRAMES_IN_SEC = 50

MAX_DURATION = 1
MIN_DURATION = 0.1
DIFF_DURATION = 0.1
NUM_OF_BITS = 8

current_frame = 0
duration = 0.6
animations = []

faster = False
slower = True

smallSheep = SmallSheep()
bigSheep12 = BigSheep12()
bigSheep34 = BigSheep34()

########################################################
# button defs
########################################################

# must divide 5 * NUM_OF_BITS
SLOW_BUTTON_FRAMES = 20
FAST_BUTTON_FRAMES = 80

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)


def lit_button1():
    GPIO.output(4, GPIO.HIGH)
    return


def lit_button2():
    GPIO.output(27, GPIO.HIGH)
    return


def unlit_button1():
    GPIO.output(4, GPIO.LOW)
    return


def unlit_button2():
    GPIO.output(27, GPIO.LOW)
    return


def btn1_clicked():
    global faster
    faster = True


def btn2_clicked():
    global slower
    slower = True


GPIO.add_event_detect(17, GPIO.FALLING,
                      callback=btn1_clicked, bouncetime=300)
GPIO.add_event_detect(22, GPIO.FALLING,
                      callback=btn2_clicked, bouncetime=300)


########################################################
# animations
########################################################

def config_new_animation():
    print "duration - " + str(duration)
    global current_frame
    current_frame = 0
    animationType = random.randrange(1, 8)

    if (animationType == 0):
            show_spinning_head_animation()
    elif (animationType == 1):
            show_fade_in_out_animation()
    elif (animationType == 2):
            show_alternate_animation()
    elif (animationType == 3):
            show_sheep_confetti_animation()
    elif (animationType == 4):
            show_rainbow_animation()
    elif (animationType == 5):
            show_snake_animation()
    elif (animationType == 6):
            show_broken_animation()
    else:
            show_fibonacci_animation()


def num_of_blocks(self, original, div):
        while original % div != 0:
                div = div / 2
        return original / div


def show_alternate_animation():
        print "alternate"
        hue1 = random.random()
        hue2 = Colors.reduce_by_1(hue1 + 0.333)
        hue3 = Colors.reduce_by_1(hue1 + 0.666)

        global animations
        animations = [AlternateAnimation(smallSheep, NUM_OF_BITS / 4, hue2),
                      AlternateAnimation(bigSheep12, NUM_OF_BITS / 4, hue1),
                      AlternateAnimation(bigSheep34, NUM_OF_BITS / 4, hue3)]


def show_fade_in_out_animation():
        print "fade_in_out"
        hue1 = random.random()
        hue2 = Colors.reduce_by_1(hue1 + 0.111)
        hue3 = Colors.reduce_by_1(hue1 + 0.222)

        global animations
        animations = [FadeInOutAnimation(smallSheep, NUM_OF_BITS / 2, hue2),
                      FadeInOutAnimation(bigSheep12, NUM_OF_BITS / 2, hue1),
                      FadeInOutAnimation(bigSheep34, NUM_OF_BITS / 2, hue3)]


def show_sheep_confetti_animation():
        print "confetti"
        leds_per_cycle = 0.02

        global animations
        animations = [SheepConfettiAnimation(smallSheep, leds_per_cycle),
                      SheepConfettiAnimation(bigSheep12, leds_per_cycle),
                      SheepConfettiAnimation(bigSheep34, leds_per_cycle)]


def show_rainbow_animation():
        print "rainbow"
        global animations
        animations = [RainbowAnimation(smallSheep, NUM_OF_BITS / 4),
                      RainbowAnimation(bigSheep12, NUM_OF_BITS / 4),
                      RainbowAnimation(bigSheep34, NUM_OF_BITS / 4)]


def show_snake_animation():
        print "snake"
        global animations
        animations = [SnakeAnimation(smallSheep, NUM_OF_BITS / 4),
                      SnakeAnimation(bigSheep12, NUM_OF_BITS / 4),
                      SnakeAnimation(bigSheep34, NUM_OF_BITS / 4)]


def show_spinning_head_animation():
        print "spinning head"
        hue = random.random()

        global animations
        animations = [SpinningHeadAnimation(smallSheep, hue, NUM_OF_BITS),
                      SpinningHeadAnimation(bigSheep12, hue, NUM_OF_BITS),
                      SpinningHeadAnimation(bigSheep34, hue, NUM_OF_BITS)]


def show_fibonacci_animation():
        print "fibonacci"
        hue1 = random.random()
        hue2 = Colors.reduce_by_1(hue1 + 0.111)
        hue3 = Colors.reduce_by_1(hue1 + 0.222)

        global animations
        animations = [FibonacciAnimation(smallSheep, NUM_OF_BITS / 8, hue2),
                      FibonacciAnimation(bigSheep12, NUM_OF_BITS / 8, hue1),
                      FibonacciAnimation(bigSheep34, NUM_OF_BITS / 8, hue3)]


def show_broken_animation():
        print "broken"

        global animations
        animations = [BrokenAnimation(smallSheep, NUM_OF_BITS / 2, 3),
                      BrokenAnimation(bigSheep12, NUM_OF_BITS / 2, 6),
                      BrokenAnimation(bigSheep34, NUM_OF_BITS / 2, 6)]


########################################################
# main
########################################################

while True:

    current_frame += 1
    total_num_of_frames = int(duration * NUM_OF_BITS * FRAMES_IN_SEC)

    # animation ended
    if (current_frame == total_num_of_frames):
        config_new_animation()

    # slower animation
    if slower:
        slower = False
        duration = min(MAX_DURATION, duration + DIFF_DURATION)
        total_num_of_frames = int(duration * NUM_OF_BITS * FRAMES_IN_SEC)
        config_new_animation()

    # faster animation
    if faster:
        faster = False
        duration = max(MIN_DURATION, duration - DIFF_DURATION)
        total_num_of_frames = int(duration * NUM_OF_BITS * FRAMES_IN_SEC)
        config_new_animation()

    # apply animations
    time_percent = float(current_frame) / total_num_of_frames
    for animation in animations:
        animation.apply(time_percent)

    # send data
    networking.send(current_frame,
                    smallSheep.get_array(),
                    bigSheep12.get_array(),
                    bigSheep34.get_array())

    # light buttons
    slow_on = math.floor(current_frame / SLOW_BUTTON_FRAMES) % 2 == 0
    if slow_on:
        lit_button1()
    else:
        unlit_button1()
    fast_on = math.floor(current_frame / FAST_BUTTON_FRAMES) % 2 == 0
    if fast_on:
        lit_button2()
    else:
        unlit_button2()

    sleep(1.0 / FRAMES_IN_SEC)  # 50 frames in seconds