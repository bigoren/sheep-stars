from AbstractSheepAnimation import SheepAnimation
from Effects.AlwaysOnEffect import AlwaysOnEffect
from Effects.BlinkEffect import BlinkEffect
from Effects.FadeInEffect import FadeInEffect

class BlinkCircleAnimation(SheepAnimation):
    def __init__(self, sheep, num_of_frames, color):
        SheepAnimation.__init__(self, sheep, num_of_frames)
        self.color = color
        self.effects = []
        self.currentBlinkBodyNum = -1;
    
    def apply(self, current_frame, parent_array):
        if (current_frame % self.num_of_frames == 0):
            self.currentBlinkBodyNum += 1
            if (self.currentBlinkBodyNum == self.sheep.get_num_of_body_parts()):
                self.currentBlinkBodyNum = 0;

            headColor = [self.color[1], self.color[2],self.color[0]]
            legColor = [self.color[2], self.color[0],self.color[1]]
            bodyColor = [int(self.color[0]*0.1), int(self.color[1]*0.1), int(self.color[2]*0.1)]

            headEffect = AlwaysOnEffect(self.sheep.get_head_indexes(), self.num_of_frames, headColor)
            legEffect = AlwaysOnEffect(self.sheep.get_legs_indexes(), self.num_of_frames, legColor)
            bodyEffect = AlwaysOnEffect(self.sheep.get_body_indexes(), self.num_of_frames, bodyColor)

            lastIndex = self.sheep.get_num_of_body_parts()-1 if self.currentBlinkBodyNum == 0 else self.currentBlinkBodyNum-1
            fadeInEffect = FadeInEffect(self.sheep.get_body_part_indexes(lastIndex), self.num_of_frames, bodyColor)

            blinkEffect = BlinkEffect(self.sheep.get_body_part_indexes(self.currentBlinkBodyNum), self.num_of_frames, self.color)

            self.effects = [headEffect,legEffect, bodyEffect, fadeInEffect, blinkEffect]
        
        for effect in self.effects:
            effect.apply(current_frame, parent_array)
