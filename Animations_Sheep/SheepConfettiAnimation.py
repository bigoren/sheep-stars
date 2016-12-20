from AbstractSheepAnimation import SheepAnimation
from Effects.ConfettiEffect import ConfettiEffect

class SheepConfettiAnimation(SheepAnimation):
    def __init__(self, sheep, time_on):
        SheepAnimation.__init__(self, sheep, time_on)
        self.effects = [ConfettiEffect(self.sheep.get_all_indexes(), self.time_on, 2) ]
    
    def apply(self, current_time, parent_array):
        for effect in self.effects:
            effect.apply(current_time, self.sheep.arr)
