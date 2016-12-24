from AbstractSheepAnimation import SheepAnimation
from Effects.FadingSnakeEffect import FadingSnakeEffect

class SnakeAnimation(SheepAnimation):
    def __init__(self, sheep):
        SheepAnimation.__init__(self, sheep)
        self.effects = [
            FadingSnakeEffect(self.sheep.get_head_indexes(), 0.1),
            FadingSnakeEffect(self.sheep.get_inner_ear_indexes(), 0.5),
            FadingSnakeEffect(self.sheep.get_outer_ear_indexes(), 0.5),
            FadingSnakeEffect(self.sheep.get_body_indexes(), 0.8)]
    
    def apply(self, time_percent):
        for effect in self.effects:
            effect.apply(time_percent, self.sheep.get_array())
