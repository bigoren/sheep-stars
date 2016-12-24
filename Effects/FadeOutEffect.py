from AbstractEffect import Effect

class FadeOutEffect(Effect):
    def __init__(self, indexes, color):
        Effect.__init__(self, indexes)
        self.color = color
    
    def apply(self, time_percent, parent_array):
        for i in self.indexes:
            parent_array[i*3 : i*3+3] = [
                int(self.color[0] * (1-time_percent)),
                int(self.color[1] * (1-time_percent)),
                int(self.color[2] * (1-time_percent))]


