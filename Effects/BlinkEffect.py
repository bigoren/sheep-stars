from AbstractEffect import Effect

class BlinkEffect(Effect):
    def __init__(self, indexes, num_of_frames, color):
        Effect.__init__(self, indexes, num_of_frames)
        self.color = color
    
    def apply(self, current_frame, parent_array):
        for i in self.indexes:
            current_frame = current_frame % self.num_of_frames
            if (current_frame < self.num_of_frames/2):
                parent_array[i*3 : i*3+3] = self.color
            else:
                parent_array[i*3 : i*3+3] = [0,0,0]


