import RPi.GPIO as GPIO
from time import sleep
#from hallon import button_pressed

########################################################
# setup GPIO
########################################################

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(4, GPIO.OUT)

########################################################
# button defs
########################################################

def lit_button():
    GPIO.output(4, GPIO.HIGH)

def unlit_button():
    GPIO.output(4, GPIO.LOW)

def button_is_pressed():
    return GPIO.input(17)

########################################################
# start the app
########################################################

lit_button()
print "button is on waiting for press"

while 1:
    if button_is_pressed():
        print "button pressed! turning led off"
        unlit_button()
        sleep(2)
        #button_pressed()
        print "turning led back on"
        lit_button()
    sleep(1)
    # print "button off"
    # unlit_button()
    # sleep(1)
    # print "button_on"
    # lit_button()