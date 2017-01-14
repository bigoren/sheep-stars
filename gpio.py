import RPi.GPIO as GPIO
from time import sleep
#from hallon import button_pressed

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

def lit_button():
    GPIO.output(4, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)

def unlit_button():
    GPIO.output(4, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)

def button1_is():
    return GPIO.input(17)

def button2_is():
    return GPIO.input(22)


def run(sleep_time=0.5):
    lit_button()
    print "buttons are on waiting for press"
    flag = 1
    delay_cycles = 0

    while 1:
        if (delay_cycles == 0):
            if flag:
                #print "light button"
                lit_button()
                flag = 0
            else:
                #print "unlight button"
                unlit_button()
                flag = 1
            
            if button1_is():
                print "button 1 pushed! "
            if button2_is():    
                print "button 2 pushed! "
            if (button1_is() and button2_is()):
                delay_cycles = 50
                print "Double PUSH! Disable buttons for "+str(delay_cycles*sleep_time)
                unlit_button()

        else:
            delay_cycles = delay_cycles - 1
        
        sleep(sleep_time)
########################################################
# start the app
########################################################

run(0.5)

