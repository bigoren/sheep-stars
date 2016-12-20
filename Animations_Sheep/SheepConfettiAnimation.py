from AbstractSheepAnimation import SheepAnimation
from Effects.ConfettiEffect import ConfettiEffect

class SheepConfettiAnimation(SheepAnimation):
    def __init__(self, sheep, num_of_frames):
        SheepAnimation.__init__(self, sheep, num_of_frames)
        self.effects = [ConfettiEffect(self.sheep.get_head_indexes(), self.num_of_frames, 2) ]
    
    def apply(self, current_frame, parent_array):
        for effect in self.effects:
            effect.apply(current_frame, parent_array)
