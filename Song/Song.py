import pygame
import math
import random

import networking_may as networking

from Colors import Colors

from UIElements.SmallSheep import SmallSheep
from UIElements.BigSheep34 import BigSheep34
from UIElements.BigSheep12 import BigSheep12

from Animations_Sheep.SpinningHeadAnimation import SpinningHeadAnimation
from Animations_Sheep.SheepConfettiAnimation import SheepConfettiAnimation
from Animations_Sheep.RainbowAnimation import RainbowAnimation
from Animations_Sheep.FadeInOutAnimation import FadeInOutAnimation
from Animations_Sheep.AlternateAnimation import AlternateAnimation
from Animations_Sheep.SnakeAnimation import SnakeAnimation

class Song(object):
    
        def __init__(self):
                self.smallSheep = SmallSheep()
                self.bigSheep12 = BigSheep12()
                self.bigSheep34 = BigSheep34()

                self.current_block_num = -1;
                
                self.animations = []
                self.plan = []
      
                self.cycle_num = 0

        def play(self):
                cycle_num = 0
                
                pygame.mixer.init()
                pygame.mixer.music.load(self.file)
                pygame.mixer.music.play(0)

                clock = pygame.time.Clock()
                while pygame.mixer.music.get_busy():
                        song_time = pygame.mixer.music.get_pos()
                        #song_time = song_time/1000.0
                        song_time = max(song_time/1000.0 - 0.6, 0)
                        self.apply_animations(song_time)
                        networking.send(cycle_num,
                                        self.smallSheep.get_array(),
                                        self.bigSheep12.get_array(),
                                        self.bigSheep34.get_array())
                        clock.tick(50)

                cycle_num += 1

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
                print str(block_num) + " - " + str(current_block)
                if current_block[2] == 'S':
                        self.strong_animation(current_block)
                else:
                       self.weak_animation(current_block)
              
            percent = (current_time - current_block[0]) / current_block[3]
            for animation in self.animations:
                animation.apply(percent)


        def num_of_blocks(self, original, div):
                while original % div != 0:
                        div = div/2
                return original/div

        def show_alternate_animation(self, current_block):
                num_of_blocks = current_block[1]
                if current_block[2] == 'W':
                        num_of_blocks = self.num_of_blocks(num_of_blocks , 2)

                hue1 = random.random()
                hue2 = hue1
                hue3 = hue1
                
                if current_block[2] == 'S':
                        hue2 = Colors.reduce_by_1(hue1+0.333)
                        hue3 = Colors.reduce_by_1(hue1+0.666)
                        
                self.animations = [
                        AlternateAnimation(self.smallSheep, num_of_blocks, hue2),
                        AlternateAnimation(self.bigSheep12, num_of_blocks, hue1),
                        AlternateAnimation(self.bigSheep34, num_of_blocks, hue3)]
        
        def weak_animation(self, current_block):
                num_of_blocks1 = current_block[1]
                num_of_blocks2 = self.num_of_blocks(num_of_blocks1 , 2)
                num_of_blocks4 = self.num_of_blocks(num_of_blocks1 , 4)
                num_of_blocks8 = self.num_of_blocks(num_of_blocks1 , 8)

                color1 = Colors.get_random_color()
                color2 = Colors.opposite_color(color1)

                typeW = random.randrange(5)
                self.animations = [
                    SnakeAnimation(self.smallSheep),
                    SnakeAnimation(self.bigSheep12),
                    SnakeAnimation(self.bigSheep34)]
                return
                        
                if (typeW == 0):
                    self.animations = [
                        SpinningHeadAnimation(self.smallSheep, color1, num_of_blocks4),
                        SpinningHeadAnimation(self.bigSheep12, color2, num_of_blocks4),
                        SpinningHeadAnimation(self.bigSheep34, color1, num_of_blocks4)]

                elif (typeW == 1):
                    self.animations = [
                        FadeInOutAnimation(self.smallSheep, num_of_blocks2),
                        FadeInOutAnimation(self.bigSheep12, num_of_blocks2),
                        FadeInOutAnimation(self.bigSheep34, num_of_blocks2)]

                elif (typeW == 2):
                    self.show_alternate_animation(current_block)

                elif (typeW == 3):
                    self.animations = [
                        SheepConfettiAnimation(self.smallSheep),
                        SheepConfettiAnimation(self.bigSheep12),
                        SheepConfettiAnimation(self.bigSheep34)]

                else:
                    self.animations = [
                        RainbowAnimation(self.smallSheep, num_of_blocks4),
                        RainbowAnimation(self.bigSheep12, num_of_blocks4),
                        RainbowAnimation(self.bigSheep34, num_of_blocks4)]

        def strong_animation(self, current_block):
                num_of_blocks1 = current_block[1]
                num_of_blocks2 = self.num_of_blocks(num_of_blocks1 , 2)
                num_of_blocks4 = self.num_of_blocks(num_of_blocks1 , 4)
                num_of_blocks8 = self.num_of_blocks(num_of_blocks1 , 8)

                color1 = Colors.get_random_color()
                color2 = Colors.opposite_color(color1)

                typeS = random.randrange(5)

                self.animations = [
                    SnakeAnimation(self.smallSheep),
                    SnakeAnimation(self.bigSheep12),
                    SnakeAnimation(self.bigSheep34)]
                return
                
                if (typeS == 0):
                    self.animations = [
                        SpinningHeadAnimation(self.smallSheep, color1, num_of_blocks),
                        SpinningHeadAnimation(self.bigSheep12, color2, num_of_blocks),
                        SpinningHeadAnimation(self.bigSheep34, color1, num_of_blocks)]

                elif (typeS == 1):
                    self.animations = [
                        FadeInOutAnimation(self.smallSheep, num_of_blocks),
                        FadeInOutAnimation(self.bigSheep12, num_of_blocks),
                        FadeInOutAnimation(self.bigSheep34, num_of_blocks)]

                elif (typeS == 2):
                        self.show_alternate_animation(current_block)

                elif (typeS == 3):
                    self.animations = [
                        SheepConfettiAnimation(self.smallSheep),
                        SheepConfettiAnimation(self.bigSheep12),
                        SheepConfettiAnimation(self.bigSheep34)]

                else:
                    self.animations = [
                        RainbowAnimation(self.smallSheep, num_of_blocks2),
                        RainbowAnimation(self.bigSheep12, num_of_blocks2),
                        RainbowAnimation(self.bigSheep34, num_of_blocks2)]
                    

