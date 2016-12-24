import math
from AbstractEffect import Effect

class FadeOutEffect(Effect):
    def __init__(self, indexes, color):
        Effect.__init__(self, indexes)
        self.color = color
    
    def apply(self, time_percent, parent_array):
        power = math.pow(1-time_percent, 3)
        for i in self.indexes:
            parent_array[i*3 : i*3+3] = [
                int(self.color[0] * power),
                int(self.color[1] * power),
                int(self.color[2] * power)]


