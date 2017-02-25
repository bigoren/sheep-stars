import math
import colorsys
from Colors import Colors
import random

from UIElements.Flower import Flower
from Effects.AlternateColorEvery3Effect import AlternateColorEvery3Effect
from Effects.AdvanceEffect import AdvanceEffect

class AlternateFlowerAnimation():

    def __init__(self, flower, num_of_spins, starting_hue):
        self.flower = flower
        self.num_of_spins = num_of_spins
        self.current_spin = -1
        self.hue1 = starting_hue
    
    def create_effects(self):
        
        leavesEffect = AlternateColorEvery3Effect(self.flower.get_leaves(), self.current_color1, self.current_color2)
        indexes = self.flower.get_seeds()
        random.shuffle(indexes)
        seedsEffect = AdvanceEffect.initColor(indexes, self.current_color2, self.current_color1)
    
        self.effects = [leavesEffect, seedsEffect]
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        if (spin != self.current_spin):
            self.current_spin = spin
            self.hue1 = Colors.reduce_by_1(self.hue1 + 0.4)
            self.hue2 = Colors.reduce_by_1(self.hue1+0.25)
            self.current_color1 = [int(c*255) for c in colorsys.hsv_to_rgb(self.hue1, 1.0, 0.15)]
            self.current_color2 = [int(c*255) for c in colorsys.hsv_to_rgb(self.hue2, 1.0, 0.15)]
            self.create_effects()

        oneSpinTime = 1.0 / self.num_of_spins
        relativePercent = (time_percent - oneSpinTime * self.current_spin) * self.num_of_spins
        for effect in self.effects:
            effect.apply(relativePercent, self.flower.get_array())
