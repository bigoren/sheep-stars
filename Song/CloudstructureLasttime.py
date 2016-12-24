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

class CloudstructureLasttime(Song):

        def __init__(self):
                super(CloudstructureLasttime, self).__init__()
                self.file = 'Music/cloudstructure-lasttime.mp3'
                self.current_block_num = -1;
                self.smallSheep = SmallSheep()
                
                self.animations = []
                self.plan = [[0.0, 8, 'W', 6.666], [6.666, 20, 'W', 16.667], [23.333, 36, 'W', 30.0], [53.333, 28, 'S', 23.333], [76.666, 2, 'W', 1.667], [78.333, 6, 'W', 0.833], [79.166, 4, 'W', 0.209], [79.375, 2, 'W', 0.625], [80.0, 24, 'S', 20.0], [100.0, 4, 'W', 3.333], [103.333, 8, 'W', 3.333], [106.666, 28, 'S', 23.334], [130.0, 4, 'S', 3.333], [133.333, 28, 'S', 23.333], [156.666, 4, 'S', 3.334], [160.0, 8, 'W', 6.666], [166.666, 4, 'W', 3.334], [170.0, 4, 'S', 3.333], [173.333, 28, 'S', 23.333], [196.666, 8, 'S', 3.334], [200.0, 16, 'S', 13.333], [213.333, 12, 'S', 10.0], [223.333, 4, 'W', 3.333], [226.666, 16, 'S', 13.334], [240.0, 12, 'S', 10.0], [250.0, 2, 'W', 1.666], [251.666, 4, 'W', 1.667], [253.333, 16, 'S', 13.333], [266.666, 4, 'S', 3.334], [270.0, 8, 'W', 6.666], [276.666, 2, 'W', 1.667], [278.333, 4, 'W', 1.667], [280.0, 8, 'S', 6.666], [286.666, 16, 'S', 13.334], [300.0, 4, 'S', 3.333], [303.333, 6, 'W', 1.25], [304.583, 10, 'W', 2.083], [306.666, 28, 'S', 23.334], [330.0, 8, 'S', 3.333], [333.333, 16, 'S', 13.333], [346.666, 16, 'S', 13.318], [359.984, 16, 'W', 13.016], [373.0, 14, 'S', 11.2], [384.2, 4, 'W', 1.6], [385.8, 16, 'S', 12.8], [398.6, 32, 'S', 25.6], [424.2, 32, 'S', 25.6], [449.8, 32, 'S', 25.6], [475.4, 32, 'S', 25.6], [501.0, 8, 'W', 6.4], [507.4, 8, 'W', 6.4], [513.8, 12, 'W', 9.6], [523.4, 2, 'W', 1.6], [525.0, 4, 'W', 1.6], [526.6, 32, 'W', 25.6], [552.2, 16, 'S', 12.8], [565.0, 16, 'S', 12.8], [577.8, 16, 'S', 12.8], [590.6, 12, 'S', 9.6], [600.2, 4, 'W', 28.8], [629.0, 32, 'S', 25.6], [654.6, 8, 'S', 12.8], [667.4, 8, 'S', 12.8], [680.2, 16, 'W', 12.8], [693.0, 16, 'W', 12.8], [705.8, 32, 'W', 38.4]]

        def num_of_blocks(self, original, div):
                while original % div != 0:
                        div = div/2
                return original/div
                
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

                        num_of_blocks1 = current_block[1]
                        num_of_blocks2 = self.num_of_blocks(num_of_blocks1 , 2)
                        num_of_blocks4 = self.num_of_blocks(num_of_blocks1 , 4)
                        num_of_blocks8 = self.num_of_blocks(num_of_blocks1 , 8)
                        typeW = random.randrange(5)
                        if (typeW == 0):
                                
                            self.animations = [
                                SpinningHeadAnimation(self.smallSheep, color1, num_of_blocks2),
                                SpinningHeadAnimation(self.bigSheep12, color2, num_of_blocks2),
                                SpinningHeadAnimation(self.bigSheep34, color1, num_of_blocks2)]
                        elif (typeW == 1):
                            self.animations = [
                                FadeInOutAnimation(self.smallSheep, num_of_blocks4),
                                FadeInOutAnimation(self.bigSheep12, num_of_blocks4),
                                FadeInOutAnimation(self.bigSheep34, num_of_blocks4)]
                        elif (typeW == 2):
                            self.animations = [
                                AlternateAnimation(self.smallSheep, num_of_blocks4),
                                AlternateAnimation(self.bigSheep12, num_of_blocks4),
                                AlternateAnimation(self.bigSheep34, num_of_blocks4)]
                        elif (typeW == 3):
                            self.animations = [
                                SheepConfettiAnimation(self.smallSheep),
                                SheepConfettiAnimation(self.bigSheep12),
                                SheepConfettiAnimation(self.bigSheep34)]
                        else:
                            self.animations = [
                                RainbowAnimation(self.smallSheep, 4),
                                RainbowAnimation(self.bigSheep12, 4),
                                RainbowAnimation(self.bigSheep34, 4)]
                else:
                    self.animations = [
                        SheepConfettiAnimation(self.smallSheep),
                        SheepConfettiAnimation(self.bigSheep12),
                        SheepConfettiAnimation(self.bigSheep34)]
                    
            percent = (current_time - current_block[0]) / current_block[3]
            for animation in self.animations:
                animation.apply(percent)
