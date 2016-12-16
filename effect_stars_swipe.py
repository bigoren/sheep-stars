
import leds_effects
import star
import random

'''
we want a nice stars shine effect.
in each frame, we will light a star with a probability.
we have the total number of stars in the string, and the number of frames in total.
the amount factor is the number of stars we want to light all in all
'''

def rand_channel_color(base_intensity):
	new_channel_color = base_intensity + random.randint(-32,32)
	return max(min(new_channel_color, 255), 0)

class SingleStarEffect(leds_effects.LedsEffect):

	time_on = 0
	time_end = 50
	time_start = 50
	
	num_of_stars = 50

	def get_name(self):
		return "StarsSwipe"

	def set_parameters(self, start_frame, end_frame):
		self._start_frame = start_frame
		self._end_frame = end_frame
		self._last_star_on_frame = max(self._end_frame - (self.time_on - self.time_end), self._start_frame)
		self._num_of_on_frames = self._last_star_on_frame - self._start_frame
		unsafe_shine_prob = 0.8 * float(self.num_of_stars) / float(self._num_of_on_frames) if self._num_of_on_frames > 0 else 0
		self._shine_prob = min(max(unsafe_shine_prob, 0), 1)
	
	def params_as_dict(self):
		return {"start_frame": self._start_frame, "end_frame" : self._end_frame}
		
	def params_from_dict(self, params):
		self.set_parameters(int(params["start_frame"]), int(params["end_frame"]))
	
	def apply(self, curr_frame):
		is_on = curr_frame >= self._start_frame and curr_frame <= self._last_star_on_frame
		if is_on and random.uniform(0, 1) < self._shine_prob and self._num_of_on_frames > 0:
			curr_loc = float(curr_frame - self._start_frame) / self._num_of_on_frames
			led_index_unsafe = int(curr_loc * self.num_of_stars) + random.randint(-2,2)
			led_index_safe = min(max(led_index_unsafe, 0), self.num_of_stars - 1)
			if not star.stars[led_index_safe].is_on():
				base_intensity = random.randint(8,255-1)
				rand_color = [rand_channel_color(base_intensity), rand_channel_color(base_intensity), rand_channel_color(base_intensity)]
				star.stars[led_index_safe].set_parameters(curr_frame, self.time_start, self.time_on, self.time_end, rand_color)
		return is_on
		#self._star.set_parameters(self._begin_frame, self._start_frames, self._on_frames, self._end_frames)
	