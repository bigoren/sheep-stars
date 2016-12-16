
import config_leds

stars_array_size = config_leds.num_stars * 3
stars_buf = [0] * stars_array_size

def set_pixel(buf, index, color):
	for channel in range(0,3):
		buf[index * 3 + channel] = color[channel]

class Star:
		
	def __init__(self, index_on_arr):
		self._index_on_arr = index_on_arr
		self.turn_off()
		
	def turn_off(self):
		self._begin_frame = None
		self._start_frames = None
		self._on_frames = None
		self._end_frames = None	
	
	def is_on(self):
		return self._begin_frame is not None
	
	def set_parameters(self, curr_frame, start_frames, on_frames, end_frames, color):
		
		if self._start_frames is None: # the star is currently OFF
			self._begin_frame = curr_frame
			self._start_frames = start_frames
			self._on_frames = on_frames
			self._end_frames = end_frames
			self._color = color
			
		else: # star is currently ON, need to merge
			pass
			
	def draw(self, curr_frame):
	
		if not self.is_on():
			set_pixel(stars_buf, self._index_on_arr, [0,0,0])
			return
			
		intensity = 0
		f = curr_frame - self._begin_frame
		if f < self._start_frames:
			intensity = float(f) / self._start_frames
		elif f < (self._start_frames + self._on_frames):
			intensity = 1.0
		elif f < (self._start_frames + self._on_frames + self._end_frames):
			intensity = 1.0 - float(f - (self._start_frames + self._on_frames)) / self._end_frames
		else:
			self.turn_off()
		
		scaled_color = []
		for channel in self._color:
			scaled_color.append(int(channel * intensity))
			'''
			if intensity < 0.5:
				pix_color = int(16 * (intensity * 2.0))
			else:
				pix_color = int(16 + (255 - 16) * (intensity - 0.5))
			'''
		set_pixel(stars_buf, self._index_on_arr, scaled_color)
	

	
stars = [Star(i) for i in range(0, config_leds.num_stars)]
