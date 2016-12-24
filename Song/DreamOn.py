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

class DreamOn(Song):

        def __init__(self):
                super(DreamOn, self).__init__()
                self.file = 'Music/Dream-on.mp3'
                self.current_block_num = -1;
                self.smallSheep = SmallSheep()
                
                self.animations = []
                self.plan = [[0.0, 16, 'W', 12.347], [12.347, 16, 'W', 12.312], [24.659, 8, 'W', 6.172], [30.831, 8, 'W', 6.047], [36.878, 32, 'W', 25.126], [62.004, 8, 'W', 6.261], [68.265, 16, 'W', 6.301], [74.566, 16, 'S', 12.076], [86.642, 6, 'W', 4.651], [91.293, 4, 'W', 1.336], [92.629, 8, 'W', 6.418], [99.047, 28, 'W', 22.076], [121.123, 8, 'W', 2.781], [123.904, 8, 'S', 6.051], [129.955, 8, 'S', 5.962], [135.917, 16, 'S', 6.127], [142.044, 12, 'W', 4.578], [146.622, 2, 'W', 1.572], [148.194, 12, 'W', 4.465], [152.659, 2, 'W', 1.539], [154.198, 12, 'W', 4.643], [158.841, 2, 'W', 1.533], [160.374, 4, 'W', 3.063], [163.437, 8, 'S', 6.073], [169.51, 8, 'S', 5.95], [175.46, 16, 'W', 5.319], [180.779, 4, 'W', 0.776], [181.555, 2, 'S', 1.463], [183.018, 2, 'S', 1.481], [184.499, 2, 'S', 1.52], [186.019, 2, 'S', 1.53], [187.549, 4, 'S', 3.027], [190.576, 8, 'S', 2.897], [193.473, 8, 'S', 5.84], [199.313, 6, 'S', 4.437], [203.75, 8, 'S', 1.397], [205.147, 2, 'W', 1.458], [206.605, 4, 'W', 1.483], [208.088, 2, 'S', 1.41], [209.498, 4, 'W', 1.508], [211.006, 2, 'S', 1.461], [212.467, 4, 'W', 1.44], [213.907, 8, 'W', 1.422], [215.329, 4, 'S', 1.509], [216.838, 16, 'W', 6.005], [222.843, 8, 'S', 5.904], [228.747, 16, 'S', 11.711], [240.458, 16, 'S', 5.849], [246.307, 32, 'W', 5.916], [252.223, 4, 'S', 18.227]]
                
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
