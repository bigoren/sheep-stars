from UIElements.Flower import Flower
from Effects.ConfettiEffect import ConfettiEffect

class ConfettiFlowerAnimation():

    def __init__(self, flower, leds_percent_per_cycle):
        self.flower = flower
        self.effect = ConfettiEffect(self.flower.get_leaves(), leds_percent_per_cycle * 2)


    def apply(self, time_percent):
        self.effect.apply(time_percent, self.flower.get_array())
