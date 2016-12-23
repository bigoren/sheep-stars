from AbstractEffect import Effect

import colorsys
import math

class AdvanceEffect(Effect):
    
    def __init__(self, indexes, current_spin):
        Effect.__init__(self, indexes)
        self.color_now = self._get_color_from_change_id(current_spin)
        self.color_before = self._get_color_from_change_id(current_spin-1)
        print self.color_before
   
    def apply(self, time_precent, parent_array):
        
        break_index = int( len(self.indexes) * time_precent)
        
        for i in range(0, break_index):
            i_in_arr = self.indexes[i]
            parent_array[i_in_arr*3 : (i_in_arr+1)*3] = self.color_now
        
        for i in range(break_index, len(self.indexes)):
            i_in_arr = self.indexes[i]
            parent_array[i_in_arr*3 : (i_in_arr+1)*3] = self.color_before

    def _get_color_from_change_id(self, current_spin):
        hue = (current_spin / 6.5)
        while hue > 1.0:
            hue = hue - 1.0
        while hue < 0.0:
            hue = hue + 1.0
        return [int(c*255) for c in colorsys.hsv_to_rgb(hue, 0.8, 0.2)]