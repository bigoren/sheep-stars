from Song.DreamOn import DreamOnSong
import pygame

pygame.init()
pygame.display.set_mode((200,100))
pygame.mixer.init()

song1 = DreamOnSong()
song1.play()
