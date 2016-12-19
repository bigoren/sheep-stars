from AbstractEffect import Effect

class AlwaysOnEffect(Effect):
    def __init__(self, indexes, num_of_frames, color):
        Effect.__init__(self, indexes, num_of_frames)
        self.color = color
    
    def apply(self, current_frame, parent_array):
        for i in self.indexes:
            parent_array[i*3 : i*3+3] = self.color


