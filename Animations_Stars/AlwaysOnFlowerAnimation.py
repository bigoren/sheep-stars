from UIElements.Flower import Flower
from Effects.AlwaysOnEffect import AlwaysOnEffect

class AlwaysOnFlowerAnimation():

    def __init__(self, signs, color):
        self.flower = flower
        self.effects = [AlwaysOnEffect(self.flower.get_all_indexes(), color)]


    def apply(self, time_percent):
        for effect in self.effects:
            effect.apply(time_percent, self.flower.get_array())
