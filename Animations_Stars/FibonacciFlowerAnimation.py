import math
import colorsys
from Colors import Colors
from UIElements.Flower import Flower
from Effects.FibonacciEffect import FibonacciEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect

class FibonacciFlowerAnimation:

    def __init__(self, flower, num_of_spins, starting_hue):
        self.flower = flower
        self.num_of_spins = num_of_spins
        self.current_spin = -1
        self.hue = starting_hue
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        if (spin != self.current_spin):
            self.current_spin = spin
            self.hue = Colors.reduce_by_1(self.hue+0.62)
            self.effects = [AlwaysOnEffect(self.flower.get_all_indexes(), [30,30,30]),
                FibonacciEffect(self.flower.get_leaves(), self.hue)]

        oneSpinTime = 1.0 / float(self.num_of_spins)
        relativePercent = (time_percent - oneSpinTime * self.current_spin) * self.num_of_spins
        for effect in self.effects:
            effect.apply(relativePercent, self.flower.get_array())
