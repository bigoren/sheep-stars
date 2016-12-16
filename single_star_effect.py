
import leds_effects
import star

class SingleStarEffect(leds_effects.LedsEffect):

	def get_name(self):
		return "SingleStar"

	def set_parameters(self, index, begin_frame, start_frames, on_frames, end_frames):
		self._index = index
		self._begin_frame = begin_frame
		self._start_frames = start_frames
		self._on_frames = on_frames
		self._end_frames = end_frames
		self._star = star.stars[index]
	
	def params_as_dict(self):
		return {"index": self._index, "begin_frame" : self._begin_frame, "start_frames" : self._start_frames, "on_frames": self._on_frames, "end_frames": self._end_frames}
		
	def params_from_dict(self, params):
		self.set_parameters(int(params["index"]), int(params["begin_frame"]), int(params["start_frames"]), int(params["on_frames"]), int(params["end_frames"]))
	
	def apply(self, curr_frame):
		if curr_frame == self._begin_frame:
			self._star.set_parameters(self._begin_frame, self._start_frames, self._on_frames, self._end_frames)
	