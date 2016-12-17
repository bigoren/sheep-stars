
import leds_effects
import sheep

class SheepShineEffect(leds_effects.LedsEffect):

	def get_name(self):
		return "SheepShine"

	def set_parameters(self, sheep_i, begin_frame, start_frames, on_frames, end_frames):
		self._sheep_i = sheep_i
		self._begin_frame = begin_frame
		self._start_frames = start_frames
		self._on_frames = on_frames
		self._end_frames = end_frames
		self._end_frame = self._begin_frame + self._start_frames + self._on_frames + self._end_frames
		
		if sheep_i == 1:
			self._sheep = sheep.sheep_1
	
	def params_as_dict(self):
		return {"sheep_i": self._sheep_i, "begin_frame" : self._begin_frame, "start_frames" : self._start_frames, "on_frames": self._on_frames, "end_frames": self._end_frames}
		
	def params_from_dict(self, params):
		self.set_parameters(int(params["sheep_i"]), int(params["begin_frame"]), int(params["start_frames"]), int(params["on_frames"]), int(params["end_frames"]))
	
	def apply(self, curr_frame):
		if curr_frame < self._begin_frame or curr_frame > self._end_frame:
			return
			
		rel_frame = curr_frame - self._begin_frame
		intensity = 0
		if rel_frame < self._start_frames:
			intensity = float(rel_frame) / float(self._start_frames)
		else:
			rel_frame = rel_frame - self._start_frames
			if rel_frame < self._on_frames:
				intensity = 1
			else:
				rel_frame = rel_frame - self._on_frames
				intensity = float(self._on_frames - rel_frame) / float(self._end_frames)
		
		int_pixel = int(255 * intensity)
		self._sheep.set_all([int_pixel, int_pixel, int_pixel])
		
		
		
		
		
		
		
	