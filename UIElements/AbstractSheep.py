from abc import ABCMeta, abstractmethod


class Sheep:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_all_indexes(self): pass
    
    # -- Head -- ##

    @abstractmethod
    def get_head_indexes(self): pass


    # -- Body -- ##

    @abstractmethod
    def get_body_indexes(self): pass

    @abstractmethod
    def get_num_of_body_parts(self): pass

    @abstractmethod
    def get_body_part_indexes(self, body_part_number): pass


    # -- Legs -- ##

    @abstractmethod
    def get_legs_indexes(self): pass
