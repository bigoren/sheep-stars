import socket
import array
import time
import datetime

CONTROLER_IP_SMALL_SHEEP_0 = "10.0.0.213"
CONTROLER_IP_BIG_SHEEP_12 = "10.0.0.212"
CONTROLER_IP_BIG_SHEEP_34 = "10.0.0.211"
UDP_PORT = 2000

sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

def send(cycle_number,
         small_sheep0_data,
         big_sheep12_data,
         big_sheep34_data):

        header = array.array('B', [0, (cycle_number / (256 * 256) ) % 256, (cycle_number / 256) % 256, cycle_number % 256])
	pixels_data = array.array('B', small_sheep0_data)
	message_s0 = (header + pixels_data).tostring()
        
	header = array.array('B', [1, (cycle_number / (256 * 256) ) % 256, (cycle_number / 256) % 256, cycle_number % 256])
	pixels_data = array.array('B', big_sheep12_data[0:300])
	message_s1 = (header + pixels_data).tostring()
	
	header = array.array('B', [2, (cycle_number / (256 * 256) ) % 256, (cycle_number / 256) % 256, cycle_number % 256])
	pixels_data = array.array('B', big_sheep12_data[0:300])
	message_s2 = (header + pixels_data).tostring()

	header = array.array('B', [3, (cycle_number / (256 * 256) ) % 256, (cycle_number / 256) % 256, cycle_number % 256])
	pixels_data = array.array('B', big_sheep34_data[0:900])
	message_s3 = (header + pixels_data).tostring()

	header = array.array('B', [4, (cycle_number / (256 * 256) ) % 256, (cycle_number / 256) % 256, cycle_number % 256])
	pixels_data = array.array('B', big_sheep34_data[900:1800])
	message_s4 = (header + pixels_data).tostring()

        sock.sendto(message_s0, (CONTROLER_IP_SMALL_SHEEP_0, UDP_PORT))
        #sock.sendto(message_s1, (CONTROLER_IP_BIG_SHEEP_12, UDP_PORT))
        #sock.sendto(message_s2, (CONTROLER_IP_BIG_SHEEP_12, UDP_PORT))
	sock.sendto(message_s3, (CONTROLER_IP_BIG_SHEEP_34, UDP_PORT))
	sock.sendto(message_s4, (CONTROLER_IP_BIG_SHEEP_34, UDP_PORT))


