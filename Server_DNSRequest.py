
# Created by Kwabena Akoto, March 19, 2019
# 
# Uses UDP sockets and the dnspython library to send and receive DNS records
# and cache the results.
#
# Usage:
# 	
# 
# Expects to receive requests from the code, running in another Command Prompt
# 
# Required installation: pip3 install dnspython

import socket
import dns.resolver
import sys
import select

HOST = 'localhost'
PORT = 5053 # Listen port
BUFFERSIZE = 1024
GOOGLE_DNS = "8.8.8.8"
DNS_PORT = 53

# Dictionary containing questions and their corresponding DNS responses
# Should be keyed with strings like:
#   	"google.com. IN A"
# and
#   	"www.smh.com.au. IN A"
# 
# The values stored in the cache dictionary should be the responses from the
# Google DNS server at 8.8.8.8 and be of the type: dns.message.Message
cache = {}

# Dictionary containing all of the DNS queries that have been forwarded to
# the Google DNS server, AND HAVEN'T YET RECEIVED A RESPONSE. 
# When a response is received from the Google nameserver, the message 
# should be checked against the keys of this dictionary to identify if 
# the message is a response to a query in the pending_requests dictionary. 
# Hint: look for something in common between the request and response messages 
# to act as the dictionary key. 
# 
# The values stored in the pending_requests dictionary should be the addr of the
# requester (IP address and port), so that when a response is receieved, it can be 
# forwarded on to the original requester.
pending_requests = {}

def process_message(sock):
	global cache, pending_requests

	# Listen for an incoming UDP message through the socket
	data, addr = sock.recvfrom(BUFFERSIZE)
	message = dns.message.from_wire(data)

	# Make sure there is only one question in this DNS message
	if len(message.question) != 1:
		print("ERROR: More than one question in DNS query, aborting...")
		sys.exit(1)
	question = message.question[0].to_text()

	# Display whether a question or answer was received
	if len(message.answer) > 0:
		print("\nIncoming message with answer about: " + question.split(" ")[0])
	else:
		print("\nIncoming message with question about: " + question.split(" ")[0])


	# YOUR IMPLEMENTATION GOES HERE
	if len(mesage.answer) > 0:

		print("This is a response to our query.", message.id)
		print(message)
		print(addr)
		socket.sendto(message.towrite(), pending_requests[message.id] )
		
		print("NOT YET IMPLEMENTED: You still need to check if this query can be answered by the cache, if needed.", cache(message))

	print("NOT YET IMPLEMENTED: You still need to forward this request to the Google DNS server, if needed.")

	# This is just a blank message to stop the tester code waiting around for a response you havent created yet.
	# Delete this once you are sending messages back to the tester.
	sock.sendto(dns.message.Message().to_wire(), addr) 

# Open a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
	# Listen on the PORT for traffic destined to any IP address
	s.setblocking(0)
	s.bind(('', PORT))

	# Read from the socket without blocking, to allow CTRL+C to exit our program
	inputs = [s]
	outputs = []
	while inputs:
		# Waiting for a UDP message
		readable, writable, exceptional = select.select(inputs, outputs, inputs)

		for sock in readable:
			# Socket has data, read from it
			process_message(sock)

