
import leds_effects
import star
import random

def rand_channel_color(base_intensity):
	new_channel_color = base_intensity + random.randint(-32,32)
	return max(min(new_channel_color, 255), 0)

class EffectStarsGroupRandom(leds_effects.LedsEffect):

	total_stars = 50

	def get_name(self):
		return "StarsGroupRandom"

	def set_parameters(self, begin_frame, start_frames, on_frames, end_frames, num_stars):
		self._begin_frame = begin_frame
		self._start_frames = start_frames
		self._on_frames = on_frames
		self._end_frames = end_frames
		self._num_stars = num_stars
	
	def params_as_dict(self):
		return {"begin_frame": self._begin_frame, "start_frames" : self._start_frames, "on_frames" : self._on_frames, "end_frames" : self._end_frames, "num_stars" : self._num_stars}
		
	def params_from_dict(self, params):
		self.set_parameters(int(params["begin_frame"]), int(params["start_frames"]), int(params["on_frames"]), int(params["end_frames"]), int(params["num_stars"]))
	
	def apply(self, curr_frame):
		if curr_frame == self._begin_frame:
			for i in range(self._num_stars):
				led_index = random.randint(0,self.total_stars - 1)
				if not star.stars[led_index].is_on():
					base_intensity = random.randint(8,255-1)
					rand_color = [rand_channel_color(base_intensity), rand_channel_color(base_intensity), rand_channel_color(base_intensity)]
					star.stars[led_index].set_parameters(curr_frame, self._start_frames, self._on_frames, self._end_frames, rand_color)
