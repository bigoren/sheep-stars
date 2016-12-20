import networking
import pygame

from UIElements.BigSheep import s1

class Song(object):
    
	def __init__(self):
		self.animations = []
	
	def play(self):
		pygame.mixer.music.load(self.file)
		pygame.mixer.music.play(0)

		clock = pygame.time.Clock()
		while pygame.mixer.music.get_busy():
			pygame.event.poll()
			song_time = pygame.mixer.music.get_pos()
			self.apply_animations(song_time)
			networking.send(0)
			clock.tick(50)
