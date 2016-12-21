import networking_may as networking
#import networking_amir as networking
import pygame

class Song(object):
    
        def __init__(self):
                self.data = [0,0,0]*302 #may
                #self.data = [0,0,0]*600 #amir
                self.cycle_num = 0

        def play(self):
                cycle_num = 0
                
                pygame.mixer.init()
                pygame.mixer.music.load(self.file)
                pygame.mixer.music.play(0)

                clock = pygame.time.Clock()
                while pygame.mixer.music.get_busy():
                        song_time = pygame.mixer.music.get_pos()
                        self.apply_animations(song_time)
                        networking.send(cycle_num, self.data)
                        clock.tick(50)

                cycle_num += 1
