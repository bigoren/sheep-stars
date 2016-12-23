
from UIElements.BigSheep12 import BigSheep12
b = BigSheep12()
import networking_may as networking

for i in b.body[10]:
    b.arr[i*3:i*3+3] = [0, 255, 0]

networking.send(0,
                [0]*600,
                b.get_array(),
                [0]*302)


