from Colors import Colors
from AbstractSheepAnimation import SheepAnimation
from Effects.AlwaysOnEffect import AlwaysOnEffect
from Effects.SpinningFadeEffect import SpinningFadeEffect
from Effects.AlternateColorEffect import AlternateColorEffect

class SpinningHeadAnimation(SheepAnimation):

    def __init__(self, sheep, color):
        SheepAnimation.__init__(self, sheep)
        self.color = color
        self.headColor = Colors.opposite_color(self.color)
        self.legsColor1 = color#Colors.adjacent_color(self.color)[0]
        self.legsColor2 = self.headColor#Colors.adjacent_color(self.color)[1]
        
        bodyEffect = AlwaysOnEffect(self.sheep.get_body_indexes(), self.color)
        legsEffect = AlternateColorEffect(self.sheep.get_legs_indexes(), self.legsColor1, self.legsColor2)
        headEffect = SpinningFadeEffect(self.sheep.get_head_indexes(),self.headColor)
        self.effects = [bodyEffect, legsEffect, headEffect]
    
    def apply(self, time_percent, parent_array):
        
        for effect in self.effects:
            effect.apply(time_percent, parent_array)
