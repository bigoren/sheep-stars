import math
import colorsys
from Colors import Colors
from Effects.FadeInEffect import FadeInEffect
from Effects.FadeOutEffect import FadeOutEffect

class FadeInOutFlowerAnimation():

    def __init__(self, flower, num_of_spins, starting_hue):
        self.flower = flower
        self.num_of_spins = num_of_spins * 2
        self.current_spin = -1
        self.hue = starting_hue
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        if (spin != self.current_spin):
            self.current_spin = spin
            if (spin % 2 == 0):
                color1 = [int(c*255) for c in colorsys.hsv_to_rgb(self.hue, 1.0, 0.15)]
                hue2 = Colors.reduce_by_1(self.hue+0.5)
                color2 = [int(c*255) for c in colorsys.hsv_to_rgb(hue2, 1.0, 0.15)]
                self.effects = [FadeOutEffect(self.flower.get_leaves(), color1),
                                FadeOutEffect(self.flower.get_seeds(), color2)]
            else:
                self.hue = Colors.reduce_by_1(self.hue+0.29)
                color1 = [int(c*255) for c in colorsys.hsv_to_rgb(self.hue, 1.0, 0.15)]
                hue2 = Colors.reduce_by_1(self.hue+0.5)
                color2 = [int(c*255) for c in colorsys.hsv_to_rgb(hue2, 1.0, 0.15)]
                self.effects = [FadeInEffect(self.flower.get_leaves(), color1),
                                FadeInEffect(self.flower.get_seeds(), color2)]

        oneSpinTime = 1.0 / float(self.num_of_spins)
        relativePercent = (time_percent - oneSpinTime * self.current_spin) * self.num_of_spins
        for effect in self.effects:
            effect.apply(relativePercent, self.flower.get_array())
