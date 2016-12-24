import math
import random
from Song import Song
from Colors import Colors

from Animations_Sheep.SpinningHeadAnimation import SpinningHeadAnimation
from Animations_Sheep.SheepConfettiAnimation import SheepConfettiAnimation
from Animations_Sheep.RainbowAnimation import RainbowAnimation
from Animations_Sheep.FadeInOutAnimation import FadeInOutAnimation
from Animations_Sheep.AlternateAnimation import AlternateAnimation
from UIElements.SmallSheep import SmallSheep

class ChronosThought(Song):

        def __init__(self):
                super(ChronosThought, self).__init__()
                self.file = 'music/chronos-thought.mp3'
                self.current_block_num = -1;
                self.smallSheep = SmallSheep()
                
                self.animations = []
                self.plan = [[0.0, 4, 'W', 2.448], [2.448, 62, 'W', 37.96], [40.408, 32, 'S', 1.224], [41.632, 64, 'W', 39.184], [80.816, 44, 'S', 26.939], [107.755, 8, 'W', 1.224], [108.979, 16, 'S', 1.225], [110.204, 32, 'S', 19.591], [129.795, 28, 'S', 17.143], [146.938, 8, 'S', 2.449], [149.387, 36, 'S', 19.592], [168.979, 16, 'S', 9.796], [178.775, 28, 'W', 17.143], [195.918, 32, 'S', 2.449], [198.367, 32, 'S', 19.592], [217.959, 48, 'S', 29.387], [247.346, 8, 'S', 4.898], [252.244, 32, 'W', 4.898], [257.142, 32, 'S', 19.592], [276.734, 64, 'S', 39.184], [315.918, 36, 'W', 21.945], [337.863, 64, 'W', 38.414], [376.277, 64, 'W', 19.19], [395.467, 128, 'W', 38.381], [433.848, 16, 'W', 4.798], [438.646, 24, 'W', 14.392], [453.038, 128, 'W', 19.191], [472.229, 16, 'S', 19.19], [491.419, 64, 'W', 19.191], [510.61, 32, 'S', 19.19], [529.8, 32, 'W', 19.19], [548.99, 32, 'W', 19.191], [568.181, 8, 'W', 9.595], [577.776, 16, 'W', 9.595], [587.371, 64, 'W', 19.191], [606.562, 32, 'W', 19.19], [625.752, 16, 'S', 19.19], [644.942, 16, 'S', 19.191], [664.133, 16, 'S', 19.19], [683.323, 32, 'S', 19.191], [702.514, 28, 'W', 35.982]]
        def apply_animations(self, current_time):
     
            #calculate current block
            block_num = -1
            for i in range(len(self.plan)):
                block = self.plan[i]
                start_time = block[0]
                end_time = block[0] + block[3]
                if current_time >= start_time and current_time < end_time:
                    block_num = i

            current_block = self.plan[block_num]
            if (block_num != self.current_block_num):
                self.current_block_num = block_num
                print block_num
                 #new animation
                if current_block[2] == 'S' or current_block[2] == 'W':
                        color1 = Colors.get_random_color()
                        color2 = Colors.opposite_color(color1)
                        typeW = random.randrange(4)
                        typeW = 1
                        if (typeW == 0):
                            self.animations = [
                                SpinningHeadAnimation(self.smallSheep, color1, current_block[1]/2),
                                SpinningHeadAnimation(self.bigSheep12, color2, current_block[1]/2),
                                SpinningHeadAnimation(self.bigSheep34, color1, current_block[1]/2)]
                        elif (typeW == 1):
                            self.animations = [
                                FadeInOutAnimation(self.smallSheep, current_block[1]/4),
                                FadeInOutAnimation(self.bigSheep12, current_block[1]/4),
                                FadeInOutAnimation(self.bigSheep34, current_block[1]/4)]
                        elif (typeW == 2):
                            self.animations = [
                                AlternateAnimation(self.smallSheep, current_block[1]/4),
                                AlternateAnimation(self.bigSheep12, current_block[1]/4),
                                AlternateAnimation(self.bigSheep34, current_block[1]/4)]
                        elif (typeW == 3):
                            self.animations = [
                                SheepConfettiAnimation(self.smallSheep),
                                SheepConfettiAnimation(self.bigSheep12),
                                SheepConfettiAnimation(self.bigSheep34)]
                        else:
                            self.animations = [
                                RainbowAnimation(self.smallSheep, current_block[1]/4),
                                RainbowAnimation(self.bigSheep12, current_block[1]/4),
                                RainbowAnimation(self.bigSheep34, current_block[1]/4)]
                else:
                    self.animations = [
                        SheepConfettiAnimation(self.smallSheep),
                        SheepConfettiAnimation(self.bigSheep12),
                        SheepConfettiAnimation(self.bigSheep34)]
                    
            percent = (current_time - current_block[0]) / current_block[3]
            for animation in self.animations:
                animation.apply(percent)
