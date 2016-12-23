import math
import random
from Song import Song
from Colors import Colors

from Animations_Sheep.SpinningHeadAnimation import SpinningHeadAnimation
from Animations_Sheep.SheepConfettiAnimation import SheepConfettiAnimation
from Animations_Sheep.RainbowAnimation import RainbowAnimation
from UIElements.SmallSheep import SmallSheep

class FroggyWoogie(Song):

        def __init__(self):
                super(FroggyWoogie, self).__init__()
                self.file = 'music/5-Sleepy_Koala_-_Froggy_Woogie.mp3'
                self.current_block_num = -1;
                self.smallSheep = SmallSheep()
                
                self.animations = []
                self.plan = [[0.0, 32, 'W', 16.271],
                             [16.271, 16, 'S', 8.135],
                             [24.406, 44, 'S', 22.373], [46.779, 16, 'S', 8.136], [54.915, 18, 'S', 1.017], [55.932, 36, 'S', 18.305], [74.237, 14, 'S', 7.118], [81.355, 32, 'W', 16.293],
                             [97.648, 32, 'S', 16.25], [113.898, 32, 'S', 16.271], [130.169, 32, 'S', 16.271], [146.44, 64, 'S', 32.532], [178.972, 32, 'S', 16.282], [195.254, 32, 'S', 16.271],
                             [211.525, 32, 'W', 16.271], [227.796, 32, 'W', 16.271], [244.067, 32, 'W', 16.271], [260.338, 32, 'W', 16.272], [276.61, 32, 'W', 16.271], [292.881, 32, 'S', 16.271], [309.152, 32, 'S', 16.271], [325.423, 36, 'S', 18.305], [343.728, 32, 'W', 34.577]]

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
                if current_block[2] == 'W':
                    color1 = Colors.get_random_color()
                    color2 = Colors.opposite_color(color1)
                    typeW = random.randrange(2)
                    typeW = 1
                    if (typeW == 0):
                            self.animations = [
                                SpinningHeadAnimation(self.smallSheep, color1, current_block[1]/2),
                                SpinningHeadAnimation(self.bigSheep34, color2, current_block[1]/2)]
                    else:
                            self.animations = [
                                RainbowAnimation(self.smallSheep, current_block[1]/8),
                                RainbowAnimation(self.bigSheep12, current_block[1]/8),
                                RainbowAnimation(self.bigSheep34, current_block[1]/8)]
                else:
                    self.animations = [
                        SheepConfettiAnimation(self.smallSheep),
                        SheepConfettiAnimation(self.bigSheep12),
                        SheepConfettiAnimation(self.bigSheep34)]
                    
            percent = (current_time - current_block[0]) / current_block[3]
            for animation in self.animations:
                animation.apply(percent)
