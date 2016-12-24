from AbstractEffect import Effect

import colorsys
import random

class FadingSnakeEffect(Effect):
    def __init__(self, indexes, leds_per_cycle):
        Effect.__init__(self, indexes)
        self._leds_per_cycle = leds_per_cycle
        self.hue_start = random.random()
        if len(self.indexes) != 0:
            self.start_pos = random.randint(0, len(self.indexes) - 1)
    
    def apply(self, time_precent, parent_array):
        if len(self.indexes) == 0:
            return
        
        random_hue = self.hue_start + (random.random() * 0.3) - 0.3/2
        while random_hue > 1.0:
            random_hue = random_hue - 1.0
        while random_hue < 0.0:
            random_hue = random_hue + 1.0
        
        """ fade to black """
        for i in self.indexes:
            parent_array[3*i] = int(parent_array[3*i] * 0.9)
            parent_array[3*i+1] = int(parent_array[3*i+1] * 0.9)
            parent_array[3*i+2] = int(parent_array[3*i+2] * 0.9)
        
        """ add new full light color pixels """
        for _ in range(0, 1):
            pix_index = self.start_pos * 3
            parent_array[pix_index : pix_index+3] = [int(c*255) for c in colorsys.hsv_to_rgb(random_hue, 0.75, 1.0)]
            self.start_pos = (self.start_pos + 1) % len(self.indexes)
