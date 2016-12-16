
import json

class LedsEffect:
	
	def to_json(self):
		return json.dumps({"effect_name" : self.get_name(), "parameters" : self.params_as_dict() })
		
	def from_json(self, params):
		self.params_from_dict(params)		

