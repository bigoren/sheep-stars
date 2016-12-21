import socket
import array
import time
import datetime

CONTROLER_IP = "10.0.0.210"
UDP_PORT = 2000

sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

def send(cycle_number, data):

	header = array.array('B', [0, (cycle_number / (256 * 256) ) % 256, (cycle_number / 256) % 256, cycle_number % 256])
	pixels_data = array.array('B', data)
	message_s1_1 = (header + pixels_data).tostring()

	sock.sendto(message_s1_1, (CONTROLER_IP, UDP_PORT))


