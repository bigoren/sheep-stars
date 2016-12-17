from AbstractEffect import Effect

class FadeInOutEffect(Effect):
    def __init__(self, indexes, num_of_frames, color):
        Effect.__init__(self, indexes, num_of_frames)
        self.color = color
    
    def apply(self, current_frame, parent_array):
        for i in self.indexes:
            current_frame = current_frame % self.num_of_frames
            if (current_frame < self.num_of_frames / 2):
                power = current_frame / float(self.num_of_frames / 2)
            else:
                power = (self.num_of_frames - current_frame) / float(self.num_of_frames / 2)
            parent_array[i*3 : i*3+3] = [int(self.color[0] * power),
                                        int(self.color[1] * power),
                                        int(self.color[2] * power)]


