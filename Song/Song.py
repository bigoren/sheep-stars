import networking_may as networking
#import networking_amir as networking
import pygame
from UIElements.SmallSheep import SmallSheep
from UIElements.BigSheep34 import BigSheep34
from UIElements.BigSheep12 import BigSheep12

class Song(object):
    
        def __init__(self):
                self.smallSheep = SmallSheep()
                self.bigSheep12 = BigSheep12()
                self.bigSheep34 = BigSheep34()
      
                self.cycle_num = 0

        def play(self):
                cycle_num = 0
                
                pygame.mixer.init()
                pygame.mixer.music.load(self.file)
                pygame.mixer.music.play(0)

                clock = pygame.time.Clock()
                while pygame.mixer.music.get_busy():
                        song_time = pygame.mixer.music.get_pos()
                        song_time = song_time/1000.0
                        self.apply_animations(song_time)
                        networking.send(cycle_num,
                                        self.smallSheep.get_array(),
                                        self.bigSheep12.get_array(),
                                        self.bigSheep34.get_array())
                        clock.tick(50)

                cycle_num += 1
