from AbstractEffect import Effect

class SpinningFadeEffect(Effect):
    def __init__(self, indexes, num_of_frames, color):
        Effect.__init__(self, indexes, num_of_frames)
        self.color = color
        self.switch = int(num_of_frames/float(len(indexes)))
        self.currentOnLed = -1;
    
    def apply(self, current_frame, parent_array):
        current_frame = current_frame % self.num_of_frames
        
        # change current led index
        if (current_frame % self.switch == 0):
            self.currentOnLed = self.currentOnLed + 1
            if (self.currentOnLed == len(self.indexes)):
                self.currentOnLed = 0
        
        for i in range(0,len(self.indexes)):
            
            # calculate distance from current led
            if (i < self.currentOnLed):
                distance = min(self.currentOnLed - i, i + len(self.indexes) - self.currentOnLed)
            else:
                distance = min(i - self.currentOnLed, self.currentOnLed + len(self.indexes) - i)
                
            # calcuate color power based on distance
            power = 1 - 2*distance / float(len(self.indexes))
            power = pow(power,4)
            
            # apply
            parent_array[self.indexes[i]*3 : self.indexes[i]*3+3] = [int(self.color[0] * power),
                                                                     int(self.color[1] * power),
                                                                     int(self.color[2] * power)]




