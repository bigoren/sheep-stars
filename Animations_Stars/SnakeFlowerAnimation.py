from UIElements.Flower import Flower
from Effects.FadingSnakeEffect import FadingSnakeEffect
from Effects.ConfettiEffect import ConfettiEffect

import math
import random

class SnakeFlowerAnimation:
    def __init__(self, flower, num_of_spins):
        self.flower = flower
        self.num_of_spins = num_of_spins
        self.effects = [
            ConfettiEffect(self.flower.get_seeds(), 0.1),
            FadingSnakeEffect(self.flower.get_leaves(), 1)]
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        oneSpinTime = 1.0 / float(self.num_of_spins)
        relativePercent = (time_percent - oneSpinTime * spin) * self.num_of_spins
        for effect in self.effects:
            effect.apply(relativePercent, self.flower.get_array())
        
