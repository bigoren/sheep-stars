from abc import ABCMeta, abstractmethod
from UIElements.AbstractSheep import Sheep

class SheepAnimation:
    __metaclass__ = ABCMeta
    
    def __init__(self, sheep, num_of_frames):
        self.sheep = sheep
        self.num_of_frames = num_of_frames
    
    @abstractmethod
    def apply(self, current_frame, parent_array): pass

