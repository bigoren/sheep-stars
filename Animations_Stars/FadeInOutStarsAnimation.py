import math
import colorsys
import random
from Colors import Colors
from AbstractStarsAnimation import AbstractStarsAnimation
from Effects.FadeInEffect import FadeInEffect
from Effects.FadeOutEffect import FadeOutEffect

class FadeInOutStarsAnimation(AbstractStarsAnimation):

    def __init__(self, stars, num_of_spins, starting_hue):
        AbstractStarsAnimation.__init__(self, stars)
        self.num_of_spins = num_of_spins * 2
        self.current_spin = -1
        self.hue = starting_hue
        self.stars_to_apply = []
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        if (spin != self.current_spin):
            self.current_spin = spin
            if (spin % 2 == 0):
                color = [int(c*255) for c in colorsys.hsv_to_rgb(self.hue, 1.0, 0.25)]
                self.effects = [FadeOutEffect(self.stars_to_apply, color)]
            else:
                self.stars.clear()
                self.stars_to_apply = [i for i in range(0, self.stars.num_of_stars()) if random.random() < 0.2]
                self.hue = Colors.reduce_by_1(self.hue+0.29)
                color = [int(c*255) for c in colorsys.hsv_to_rgb(self.hue, 1.0, 0.25)]
                self.effects = [FadeInEffect(self.stars_to_apply, color)]

        oneSpinTime = 1.0 / float(self.num_of_spins)
        relativePercent = (time_percent - oneSpinTime * self.current_spin) * self.num_of_spins
        for effect in self.effects:
            effect.apply(relativePercent, self.stars.get_array())
