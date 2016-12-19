
import random

import leds_effects
import sheep

class LegsColorMove(leds_effects.LedsEffect):

	def get_name(self):
		return "LegsColorMove"

	def set_parameters(self, sheep_i, begin_frame, on_frame, change_freq_frames):
		self._sheep_i = sheep_i
		self._begin_frame = begin_frame
		self._on_frame = on_frame
		self._change_freq_frames = change_freq_frames
		
		self._curr_color = [0,0,0]
		self._next_color = [0,0,0]
		
		if sheep_i == 1:
			self._sheep = sheep.sheep_1
	
	def params_as_dict(self):
		return {"sheep_i": self._sheep_i, "begin_frame" : self._begin_frame, "on_frame" : self._on_frame, "change_freq_frames": self._change_freq_frames}
		
	def params_from_dict(self, params):
		self.set_parameters(int(params["sheep_i"]), int(params["begin_frame"]), int(params["on_frame"]), int(params["change_freq_frames"]))
	
	def apply(self, curr_frame):
		
		frames_since_begin = curr_frame - self._begin_frame
		if frames_since_begin < 0 or frames_since_begin >= self._on_frame:
			return
		
		if frames_since_begin % self._change_freq_frames == 0:
			self._curr_color = self._next_color
			self._next_color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]			
		
		r = (frames_since_begin % self._change_freq_frames) / float(self._change_freq_frames)

		num_leds_ll = int(r * self._sheep.ll_leg_len)
		sheep.sheep_1.set_ll_leg([self._next_color] * num_leds_ll + [self._curr_color] * (self._sheep.ll_leg_len - num_leds_ll))
		num_leds_lr = int(r * self._sheep.lr_leg_len)
		sheep.sheep_1.set_lr_leg([self._curr_color] * (self._sheep.lr_leg_len - num_leds_lr) + [self._next_color] * num_leds_lr)
		num_leds_rl = int(r * self._sheep.rl_leg_len)
		sheep.sheep_1.set_rl_leg([self._next_color] * num_leds_rl + [self._curr_color] * (self._sheep.rl_leg_len - num_leds_rl))
		num_leds_rr = int(r * self._sheep.rr_leg_len)
		sheep.sheep_1.set_rr_leg([self._curr_color] * (self._sheep.rr_leg_len - num_leds_rr) + [self._next_color] * num_leds_rr)

		
		
		
		
		
		
	