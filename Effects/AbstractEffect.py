from abc import ABCMeta, abstractmethod

class Effect:
    __metaclass__ = ABCMeta
    
    def __init__(self, indexes, num_of_frames):
        self.indexes = indexes
        self.num_of_frames = num_of_frames
    
    @abstractmethod
    def apply(self, current_frame, parent_array): pass

