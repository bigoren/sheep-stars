
import config_leds

class Sheep:

	def __init__(self):
		self.buf = None
		self.head_len = 0
		self.l_ear_len = 0
		self.r_ear_len = 0
		self.body_len = 0
		self.ll_leg_len = 0
		self.lr_leg_len = 0
		self.rl_leg_len = 0
		self.rr_leg_len = 0
		
	def set_head(self, colors):
		pass
	
	def set_l_ear(self, colors):
		pass
		
	def set_r_ear(self, colors):
		pass
		
	def set_body(self, colors):
		pass
		
	def set_ll_leg(self, colors):
		pass
		
	def set_lr_leg(self, colors):
		pass

	def set_rl_leg(self, colors):
		pass
		
	def set_rr_leg(self, colors):
		pass
		
	def set_all(self, color):
		self.set_head([color] * self.head_len)
		self.set_l_ear([color] * self.l_ear_len)
		self.set_r_ear([color] * self.r_ear_len)
		self.set_body([color] * self.body_len)
		self.set_ll_leg([color] * self.ll_leg_len)
		self.set_lr_leg([color] * self.lr_leg_len)
		self.set_rl_leg([color] * self.rl_leg_len)
		self.set_rr_leg([color] * self.rr_leg_len)
		
	def set_continues_buffer(self, colors, element_start, element_len):
		if len(colors) != element_len:
			raise
		for i in range(0, element_len):
			if len(colors[i]) != 3:
				raise
			buf_index = (element_start + i) * 3
			self.buf[buf_index : buf_index + 3] = colors[i]	

class Sheep1(Sheep):
	
	def __init__(self):
		self.buf = [0] * 600 * 3
		self.head_len = 87
		self.l_ear_len = 35
		self.r_ear_len = 40
		self.ll_leg_len = 30
		self.lr_leg_len = 30
		self.rl_leg_len = 30
		self.rr_leg_len = 28
		self.body_len = 163+58+41
		
	def set_head(self, colors):
		self.set_continues_buffer(colors, 35, self.head_len)
			
	def set_l_ear(self, colors):
		self.set_continues_buffer(colors, 0, self.l_ear_len)		

	def set_r_ear(self, colors):
		self.set_continues_buffer(colors, 560, self.r_ear_len)		

	def set_ll_leg(self, colors):
		self.set_continues_buffer(colors, 462, self.ll_leg_len)				

	def set_lr_leg(self, colors):
		self.set_continues_buffer(colors[::-1], 423, self.lr_leg_len)				
		
	def set_rl_leg(self, colors):
		self.set_continues_buffer(colors, 335, self.rl_leg_len)						

	def set_rr_leg(self, colors):
		self.set_continues_buffer(colors[::-1], 300, self.rr_leg_len)						
		
	def set_body(self, colors):
		if len(colors) != self.body_len:
			raise		
		self.set_continues_buffer(colors[0:163], 138, 163)
		self.set_continues_buffer(colors[163:(163+58)], 365, 58)
		self.set_continues_buffer(colors[(163+58):self.body_len], 492, 41)
		
sheep_1 = Sheep1()	
	