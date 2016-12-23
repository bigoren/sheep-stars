from AbstractSheepAnimation import SheepAnimation
from Effects.ConfettiEffect import ConfettiEffect

class SheepConfettiAnimation(SheepAnimation):
    def __init__(self, sheep):
        SheepAnimation.__init__(self, sheep)
        self.effects = [ConfettiEffect(self.sheep.get_all_indexes(), 2) ]
    
    def apply(self, time_percent):
        for effect in self.effects:
            effect.apply(time_percent, self.sheep.get_array())
