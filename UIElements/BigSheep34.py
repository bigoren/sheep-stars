from AbstractSheep import Sheep

class BigSheep34(Sheep):
    def __init__(self):
        self.head = range(35,122)
        self.body = [range(138,158), range(158,188), range(188,218),
                     range(218,245), range(245,272), range(272,300),
                     range(366,393), range(393,423), range(492,521),
                     range(521,533)]
					 
        self.legll = range(462,492)
        self.leglr = range(423,453)
        self.legrl = range(335,365)
        self.legrr = range(300,328)
		
        self.earl = range(0,36)
        self.earr = range(560,600)
		
        self.arr = [0,0,0] * 600

    def get_array(self):
        return self.arr
    
    def get_all_indexes(self):
        return self.get_head_indexes() + self.get_body_indexes() + self.get_legs_indexes() + self.get_ears_indexes()
    
    
    # -- Head -- #
    
    def get_head_indexes(self):
        return self.head


    # -- Body -- #
    
    def get_body_indexes(self):
        body_indexes = []
        for i in range(0, self.get_num_of_body_parts()):
            body_indexes += self.get_body_part_indexes(i)
        return body_indexes
    
    def get_num_of_body_parts(self):
        return len(self.body)
    
    def get_body_part_indexes(self, body_part_number):
        return self.body[body_part_number]

    # -- Ears -- #
    def get_ears_indexes(self):
		return self.earl + self.earr

    # -- Legs -- #
    
    def get_legs_indexes(self):
        return self.legll + self.leglr + self.legrl + self.legrr
