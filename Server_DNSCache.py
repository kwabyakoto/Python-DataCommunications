# assignment3_tester.py
# 
# IS 477/677 - Data Communications
# Spring 2019
# 
# Assignment 3 - DNS
# 
# Created by Wes Cox, March 19, 2019
# 
# Uses UDP sockets and the dnspython library to send and receive DNS records
# and cache the results.
#
# Usage:
# 	py assignment3_tester.py <hostname>
# 
# Expects to have the assignment3_server_starter.py code already running in another Command Prompt
# 
# Required installation: pip3 install dnspython

import socket
import dns.resolver
import sys

HOST = 'localhost'
DEST_PORT = 5053 # Our nameserver listens on this port
SOURCE_PORT = 6053 # This program will listen on this port
BUFFERSIZE = 1024 # bytes

# Read hostname to lookup IP address for from Command Line
if len(sys.argv) != 2:
	print("Usage: py " + sys.argv[0] + " <hostname>")
	sys.exit(1)
hostname = sys.argv[1]

# Open a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
	# Configure the socket to listen on SOURCE_PORT for traffic sent to HOST IP address
	s.bind((HOST, SOURCE_PORT))

	# Create a DNS message to query for the IP address
	msg = dns.message.make_query(hostname, "A")
	
	# Send to our nameserver
	s.sendto(msg.to_wire(), (HOST, DEST_PORT))

	# Listen for a response from the nameserver
	data, addr = s.recvfrom(BUFFERSIZE)
	message = dns.message.from_wire(data)
	if len(message.answer) == 0:
		print("No ANSWER records in response.")
	else:
		# Print the DNS answer records
		for answer in message.answer:
			print(answer.to_text())