# assignment4_starter.py
# 
# IS 477/677 - Data Communications
# Spring 2019
# 
# Assignment 4 - Reliable Data Transport
# 
# Created by Kwabena Akoto, April 8, 2019
#
# Usage:
# 	py assignment4_starter.py <message> 
# 
# Required installation: none

import sys
import random

queue_packet = []
rcvd_message = []
rcvd_sorted = []


class Packet:
	# Creates a Packet object, containing a sequence number, message and checksum
	def __init__(self, s, m):
		self.seq = s
		self.message = m
		self.checksum = len(self.message.encode('utf-8'))

	# Methods required to print a Packet object
	def __str__(self):
		return str(self.seq) + ": " + str(self.message)

	def __repr__(self):
		return str(self)

def unreliable_udp(pkt):

	num = random.randint(1,10)
	if num == 7:
		return None
	elif num == 3:
		pkt.checksum += 1
	return pkt

def unreliable(pkt):
	# Randomly drops a packet
	num = random.randint(1,10)
	if num == 7:
		print("Pakcet Lost: Resending" + pkt._seq_())
		queue_packet.append(pkt)
		return None
	else:
		rcvd_message.append(pkt)
		return pkt



def transport(m):

	# Task 2: Split the message m into words (splitting on spaces) and 
	message_list = message.split()
	# store in an array of Packet objects (packet queue) with incrementing sequence numbers
	
	# Task 3: Send each element in the packet queue through the unreliable channel (unreliable()).

	for i, msg in enumerate(message_list):
		packets = Packet(i, msg)
		queue_packet.append(packets)
	# If a packet is lost, add it to the back of the queue.

	
	# Task 4: Store packets that are successfully sent through the unreliable channel (return a string)

	while len(queue_packet) >= 1:
		queue = queue_packet.pop(0)
		post = unreliable(queue)

	# in an array in the order they are received. 
	rcvd_sorted = sorted(queue_packet, key=lamda Packet: Packet.seq)
	print(rcvd_message)
	parce = " "

	# Task 5: Sort the packets in the order of their sequence numbers
	for i, msg in enumerate(rcvd_sorted):
		parce += msg._msg_() + " "


	# Task 6: Return the messages contained in the packets, joined together by spaces, as one long string
	return parce # This will need to be replaced by the correct return statement in Task 6.

# Task 1: Check to make sure there are enough command line arguments

message = sys.argv[1]

# Send the message through the reliable transport function
rcvd_message = transport(message)
print("Received message: " + str(rcvd_message))
