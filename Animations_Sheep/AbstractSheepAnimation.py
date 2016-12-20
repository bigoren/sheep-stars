from abc import ABCMeta, abstractmethod
from UIElements.AbstractSheep import Sheep

class SheepAnimation:
    __metaclass__ = ABCMeta
    
    def __init__(self, sheep, time_on):
        self.sheep = sheep
        self.time_on = time_on
    
    @abstractmethod
    def apply(self, current_time, parent_array): pass

