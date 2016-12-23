import math
import colorsys
from Colors import Colors
from AbstractSheepAnimation import SheepAnimation
from Effects.AlternateColorEffect import AlternateColorEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect

class AlternateAnimation(SheepAnimation):

    def __init__(self, sheep, num_of_spins):
        SheepAnimation.__init__(self, sheep)
        self.num_of_spins = num_of_spins
        self.current_spin = -1
        
    def create_effects(self):
        bodyEffect = AlternateColorEffect(self.sheep.get_body_indexes(),self.current_color1,self.current_color2)
        legsEffect = AlternateColorEffect(self.sheep.get_legs_indexes(),self.current_color1,self.current_color2)
        #headEffect = AlternateEffect(self.sheep.get_head_indexes())
        self.effects = [bodyEffect, legsEffect]
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        if (spin != self.current_spin):
            self.current_spin = spin;
            hue1 = time_percent
            hue2 = hue1+0.3-1 if hue1+0.3 >= 1 else hue1+0.3
            self.current_color1 = [int(c*255) for c in colorsys.hsv_to_rgb(hue1, 1.0, 0.25)]
            self.current_color2 = [int(c*255) for c in colorsys.hsv_to_rgb(hue2, 1.0, 0.25)]
            self.create_effects()

        oneSpinTime = 1.0 / self.num_of_spins
        relativePercent = (time_percent - oneSpinTime * self.current_spin) * self.num_of_spins
        for effect in self.effects:
            effect.apply(relativePercent, self.sheep.get_array())
