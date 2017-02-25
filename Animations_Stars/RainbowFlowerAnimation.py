import math
from Colors import Colors

from UIElements.Flower import Flower
from Effects.RainbowEffect import RainbowEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect


class RainbowFlowerAnimation():

    def __init__(self, flower, num_of_spins):
        self.flower = flower
        self.num_of_spins = num_of_spins
        self.current_spin = -1
        self.effects = [RainbowEffect(self.flower.get_leaves())]
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        if (spin != self.current_spin):
            self.current_spin = spin

        oneSpinTime = 1.0 / self.num_of_spins
        relativePercent = (time_percent - oneSpinTime * self.current_spin) * self.num_of_spins
        for effect in self.effects:
            effect.apply(relativePercent, self.flower.get_array())

        seedColor = self.flower.get_array()[self.flower.get_leaves()[0]*3 :
                                            self.flower.get_leaves()[0]*3 + 3]
        seedColor = AlwaysOnEffect(self.flower.get_seeds(), seedColor)
        seedColor.apply(time_percent, self.flower.get_array())
