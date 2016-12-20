from Song import Song

from Animations_Sheep import SheepConfettiAnimation
from UIElements.BigSheep import s1

class DreamOnSong(Song):

	def __init__(self):
		self.file = r'c:\temp\DreamOnAerosmith.mp3'
		
		self.animation1 = SheepConfettiAnimation.SheepConfettiAnimation(s1, 5)
		
	def apply_animations(self, current_time):
		print current_time
		if current_time > 5 * 1000 and current_time < 10 * 1000:
			self.animation1.apply(current_time, s1.get_all_indexes())
		if current_time > 15 * 1000 and current_time < 20 * 1000:
			self.animation1.apply(current_time, s1.get_all_indexes())
		
