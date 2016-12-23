import math
from Colors import Colors
from AbstractSheepAnimation import SheepAnimation
from Effects.AlwaysOnEffect import AlwaysOnEffect
from Effects.SpinningFadeEffect import SpinningFadeEffect
from Effects.AlternateColorEffect import AlternateColorEffect
from Effects.AdvanceEffect import AdvanceEffect

class SpinningHeadAnimation(SheepAnimation):

    def __init__(self, sheep, color, num_of_spins):
        SheepAnimation.__init__(self, sheep)
        self.num_of_spins = num_of_spins
        self.current_spin = -1
        self.color = color
    
        self.headColor = Colors.opposite_color(self.color)
        self.legsColor1 = color#Colors.adjacent_color(self.color)[0]
        self.legsColor2 = self.headColor#Colors.adjacent_color(self.color)[1]
        
    def create_effects(self):
        bodyEffect = AdvanceEffect(self.sheep.get_body_indexes(), self.current_spin)
        legsEffect = AlternateColorEffect(self.sheep.get_legs_indexes(), self.legsColor1, self.legsColor2)
        headEffect = SpinningFadeEffect(self.sheep.get_head_indexes(),self.headColor)
        earlEffect = AdvanceEffect(self.sheep.earl, self.current_spin)
        earrEffect = AdvanceEffect(self.sheep.earr, self.current_spin)
        self.effects = [bodyEffect, legsEffect, headEffect, earlEffect, earrEffect]
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        if (spin != self.current_spin):
            self.current_spin = spin;
            self.create_effects()

        oneSpinTime = 1.0 / self.num_of_spins
        relativePercent = (time_percent - oneSpinTime * self.current_spin) * self.num_of_spins
        for effect in self.effects:
            effect.apply(relativePercent, self.sheep.get_array())
