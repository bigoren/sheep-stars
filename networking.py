
import socket
import array

import sheep
import star

CONTROLER_IP = "192.168.1.210"
UDP_PORT = 2000

sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

def send(cicle_number):
	header = array.array('B', [0, (cicle_number / (256 * 256) ) % 256, (cicle_number / 256) % 256, cicle_number % 256])
	pixels_data = array.array('B', star.stars_buf)
	message_0 = (header + pixels_data).tostring()

	header = array.array('B', [1, (cicle_number / (256 * 256) ) % 256, (cicle_number / 256) % 256, cicle_number % 256])
	pixels_data = array.array('B', sheep.sheep_1.buf[0:900])
	message_1 = (header + pixels_data).tostring()

	header = array.array('B', [2, (cicle_number / (256 * 256) ) % 256, (cicle_number / 256) % 256, cicle_number % 256])
	pixels_data = array.array('B', sheep.sheep_1.buf[900:1800])
	message_2 = (header + pixels_data).tostring()

	sock.sendto(message_0, (CONTROLER_IP, UDP_PORT))
	sock.sendto(message_1, (CONTROLER_IP, UDP_PORT))
	sock.sendto(message_2, (CONTROLER_IP, UDP_PORT))
	

