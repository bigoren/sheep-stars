import pygame
import math
import random
import colorsys

import networking_may as networking

from Colors import Colors

from UIElements.SmallSheep import SmallSheep
from UIElements.BigSheep34 import BigSheep34
from UIElements.BigSheep12 import BigSheep12
from UIElements.Stars import Stars

from Animations_Sheep.SpinningHeadAnimation import SpinningHeadAnimation
from Animations_Sheep.SheepConfettiAnimation import SheepConfettiAnimation
from Animations_Sheep.RainbowAnimation import RainbowAnimation
from Animations_Sheep.FadeInOutAnimation import FadeInOutAnimation
from Animations_Sheep.AlternateAnimation import AlternateAnimation
from Animations_Sheep.SnakeAnimation import SnakeAnimation
from Animations_Sheep.FibonacciAnimation import FibonacciAnimation
from Animations_Sheep.BrokenAnimation import BrokenAnimation

from Animations_Stars.FadeInOutStarsAnimation import FadeInOutStarsAnimation

class Song(object):
    
        def __init__(self):
                self.smallSheep = SmallSheep()
                self.bigSheep12 = BigSheep12()
                self.bigSheep34 = BigSheep34()
                self.stars = Stars()

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
                                        self.bigSheep34.get_array(),
                                        self.stars.get_array())
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
                self.show_random_animation(current_block)
                #self.show_fade_in_out_animation(current_block)

            percent = (current_time - current_block[0]) / current_block[3]
            for animation in self.animations:
                animation.apply(percent)

            if (block_num == len(self.plan)-1 and percent >= 0.8):
                    # fade out - end of the song
                    power = 1-(percent - 0.8)*5
                    print "fade_out " + str(power)
                    data = self.smallSheep.get_array() + self.bigSheep12.get_array() + self.bigSheep34.get_array() + self.stars.get_array()
                    for i in range(len(self.smallSheep.get_array())):
                        self.smallSheep.get_array()[i] = int(math.floor(self.smallSheep.get_array()[i] * power))
                    for i in range(len(self.bigSheep12.get_array())):
                        self.bigSheep12.get_array()[i] = int(math.floor(self.bigSheep12.get_array()[i] * power))
                    for i in range(len(self.bigSheep34.get_array())):
                        self.bigSheep34.get_array()[i] = int(math.floor(self.bigSheep34.get_array()[i] * power))
                    for i in range(len(self.stars.get_array())):
                        self.stars.get_array()[i] = int(math.floor(self.stars.get_array()[i] * power))

        def show_random_animation(self, current_block):
                animationType = random.randrange(1,8)
                        
                if (animationType == 0):
                        self.show_spinning_head_animation(current_block)
                elif (animationType == 1):
                    self.show_fade_in_out_animation(current_block)
                elif (animationType == 2):
                    self.show_alternate_animation(current_block)
                elif (animationType == 3):
                        self.show_sheep_confetti_animation(current_block)
                elif (animationType == 4):
                        self.show_rainbow_animation(current_block)
                elif (animationType == 5):
                        self.show_snake_animation(current_block)
                elif (animationType == 6):
                        self.show_broken_animation(current_block)
                else:
                        self.show_fibonacci_animation(current_block)
                        


        def num_of_blocks(self, original, div):
                while original % div != 0:
                        div = div/2
                return original/div

        def show_alternate_animation(self, current_block):
                print "alternate"
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

        def show_fade_in_out_animation(self, current_block):
                print "fade_in_out"
                num_of_blocks = current_block[1]
                if current_block[2] == 'W':
                        num_of_blocks = self.num_of_blocks(num_of_blocks , 2)

                hue1 = random.random()
                hue2 = hue1
                hue3 = hue1
                hue4 = hue1
                
                if current_block[2] == 'S':
                        hue2 = Colors.reduce_by_1(hue1+0.111)
                        hue3 = Colors.reduce_by_1(hue1+0.222)
                        hue3 = Colors.reduce_by_1(hue1+0.333)
                        
                self.animations = [
                        FadeInOutAnimation(self.smallSheep, num_of_blocks, hue2),
                        FadeInOutAnimation(self.bigSheep12, num_of_blocks, hue1),
                        FadeInOutAnimation(self.bigSheep34, num_of_blocks, hue3),
                        FadeInOutStarsAnimation(self.stars, num_of_blocks, hue4)]

        def show_sheep_confetti_animation(self, current_block):
                print "confetti"
                leds_percent_per_cycle = 0.005
                if current_block[2] == 'S':
                        leds_percent_per_cycle = 0.03
                        
                self.animations = [
                        SheepConfettiAnimation(self.smallSheep, leds_percent_per_cycle),
                        SheepConfettiAnimation(self.bigSheep12, leds_percent_per_cycle),
                        SheepConfettiAnimation(self.bigSheep34, leds_percent_per_cycle)]

        def show_rainbow_animation(self, current_block):
                print "rainbow"
                num_of_blocks = self.num_of_blocks(current_block[1], 2)
                if current_block[2] == 'W':
                        num_of_blocks = self.num_of_blocks(num_of_blocks , 4)
    
                self.animations = [
                        RainbowAnimation(self.smallSheep, num_of_blocks),
                        RainbowAnimation(self.bigSheep12, num_of_blocks),
                        RainbowAnimation(self.bigSheep34, num_of_blocks)]

        def show_snake_animation(self, current_block):
                print "snake"
                num_of_blocks = self.num_of_blocks(current_block[1], 2)
                if current_block[2] == 'W':
                        num_of_blocks = self.num_of_blocks(num_of_blocks , 4)
                        
                self.animations = [
                        SnakeAnimation(self.smallSheep, num_of_blocks),
                        SnakeAnimation(self.bigSheep12, num_of_blocks),
                        SnakeAnimation(self.bigSheep34, num_of_blocks)]

        def show_spinning_head_animation(self, current_block):
                print "spinning_head"
                num_of_blocks = self.num_of_blocks(current_block[1], 1)
                if current_block[2] == 'W':
                        num_of_blocks = self.num_of_blocks(num_of_blocks , 2)
    
                hue = random.random()
                
                self.animations = [
                        SpinningHeadAnimation(self.smallSheep, hue, num_of_blocks),
                        SpinningHeadAnimation(self.bigSheep12, hue, num_of_blocks),
                        SpinningHeadAnimation(self.bigSheep34, hue, num_of_blocks)]

        def show_fibonacci_animation(self, current_block):
                print "fibonacci"
                num_of_blocks = self.num_of_blocks(current_block[1], 2)
                if current_block[2] == 'W':
                        num_of_blocks = self.num_of_blocks(num_of_blocks , 4)

                hue1 = random.random()
                hue2 = hue1
                hue3 = hue1

                if current_block[2] == 'S':
                    hue2 = Colors.reduce_by_1(hue1+0.111)
                    hue3 = Colors.reduce_by_1(hue1+0.222)
            
                self.animations = [
                                   FibonacciAnimation(self.smallSheep, num_of_blocks, hue2),
                                   FibonacciAnimation(self.bigSheep12, num_of_blocks, hue1),
                                   FibonacciAnimation(self.bigSheep34, num_of_blocks, hue3)]

        def show_broken_animation(self, current_block):
                print "broken"
                num_of_blocks = self.num_of_blocks(current_block[1], 1)
                if current_block[2] == 'W':
                        num_of_blocks = self.num_of_blocks(num_of_blocks , 2)

                self.animations = [
                                   BrokenAnimation(self.smallSheep, num_of_blocks, 3),
                                   BrokenAnimation(self.bigSheep12, num_of_blocks, 6),
                                   BrokenAnimation(self.bigSheep34, num_of_blocks, 6)]

