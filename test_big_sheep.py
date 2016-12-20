import networking
import time

from UIElements.BigSheep import s1
from Effects.ConfettiEffect import ConfettiEffect

e = ConfettiEffect(s1.get_all_indexes(), 1000, 4)

for cycle_number in range(0,1000):
	e.apply(cycle_number, s1.arr)
	networking.send(cycle_number)
	time.sleep(1.0/50.0)
