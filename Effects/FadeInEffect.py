from AbstractEffect import Effect

class FadeInEffect(Effect):
    def __init__(self, indexes, num_of_frames, color):
        Effect.__init__(self, indexes, num_of_frames)
        self.color = color
    
    def apply(self, current_frame, parent_array):
        for i in self.indexes:
            current_frame = current_frame % self.num_of_frames
            power = current_frame / float(self.num_of_frames)
            parent_array[i*3 : i*3+3] = [int(self.color[0] * power),
                                        int(self.color[1] * power),
                                        int(self.color[2] * power)]


