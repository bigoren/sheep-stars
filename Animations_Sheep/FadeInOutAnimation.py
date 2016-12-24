import math
import colorsys
from Colors import Colors
from AbstractSheepAnimation import SheepAnimation
from Effects.FadeInEffect import FadeInEffect
from Effects.FadeOutEffect import FadeOutEffect

class FadeInOutAnimation(SheepAnimation):

    def __init__(self, sheep, num_of_spins):
        SheepAnimation.__init__(self, sheep)
        self.num_of_spins = num_of_spins * 2
        self.current_spin = -1
        self.color = [int(c*255) for c in colorsys.hsv_to_rgb(0, 1.0, 0.25)]
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        if (spin != self.current_spin):
            self.current_spin = spin
            if (spin % 2 == 0):
                self.effects = [FadeOutEffect(self.sheep.get_all_indexes(), self.color)]
            else:
                self.color = [int(c*255) for c in colorsys.hsv_to_rgb(time_percent, 1.0, 0.25)]
                self.effects = [FadeInEffect(self.sheep.get_all_indexes(), self.color)]

        oneSpinTime = 1.0 / float(self.num_of_spins)
        relativePercent = (time_percent - oneSpinTime * self.current_spin) * self.num_of_spins
        for effect in self.effects:
            effect.apply(relativePercent, self.sheep.get_array())
