from Colors import Colors
from AbstractSheepAnimation import SheepAnimation
from Effects.AlwaysOnEffect import AlwaysOnEffect
from Effects.SpinningFadeEffect import SpinningFadeEffect

class SpinningHeadAnimation(SheepAnimation):
    def __init__(self, sheep, num_of_frames, color):
        SheepAnimation.__init__(self, sheep, num_of_frames)
        self.color = color
        self.headColor = Colors.adjacent_color(self.color)[0]
        
        bodyEffect = AlwaysOnEffect(self.sheep.get_all_indexes(), self.num_of_frames, self.color)
        headEffect = SpinningFadeEffect(self.sheep.get_head_indexes(), self.num_of_frames,self.headColor)
        self.effects = [bodyEffect, headEffect]
    
    def apply(self, current_frame, parent_array):
        current_frame = current_frame % self.num_of_frames
        
        for effect in self.effects:
            effect.apply(current_frame, parent_array)
