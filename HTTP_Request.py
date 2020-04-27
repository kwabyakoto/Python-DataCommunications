# assignment2_starter.py
# 
# IS 477/677 - Data Communications
# 
# 
# Assignment 2 - HTTP
# 
# Created by Kwabena Akoto, February 23, 2019
# 
# Using the python Requests library, sends HTTP requests to the server running on
# localhost:4000
# depending on the type of request indicated by the request_num in the command
# line arguments
#
# Usage:
# 	py assignment2_start.py <request number> [additional argument]

#Request are imported into the system for command line arguments
import sys,requests

#Request 1
def request1(host):
	r = requests.get(host)
	print("Request 1: ")
	print("Status Code: " + str(r.status_code))
	print(r.text)

#Request 2
def request2(host):
	r = requests.post(host + "/login", data = {'username': 'user', 'password': 'password123'}, allow_redirects = False) 
	
	print("request 2: ")
	print("Status Code: " + str(r.status_code))
	print("Cookies: " + str(r.cookies))
	r = requests.get(host, cookies = {'logged_in' : 'true', 'secret' : 'true'})
	
	print("Status Code: " + str(r.status_code))
	print(r.text)
	
#Request 3
def request3(host, comment):
	r = requests.post(host + "/add_comment", data = {'comment': comment}, allow_redirects = False)
	print("Request 3: ")
	print("Status Code: " + str(r.status_code))
	r = requests.get(host + "/comments")
	
	print("Status Code: " + str(r.status_code))
	print(r.text)

#Request 4
def request4(host, quote):
	
	r = requests.put(host + "/quote", data = {"quote": quote}, allow_redirects = False)
	print("Request 4: ")
	print("Status Code: " + str(r.status_code))
	r = requests.get(host + "/quote")
	print("Status Code: " + str(r.status_code))
	print(r.text)
	

def request5(host, num_comments = None):
	################
	# IS 677 only
	################
	# Your implementation goes here
	print("Not yet implemented")


host_ip = "localhost"
port = "4000"

server_url = "http://" + host_ip + ":" + port

request_num = ""
additional_arg = ""

max_length = 255

# Check for required command line arguments
if len(sys.argv) in [2,3]:
	# requests 1,2,3,4,5
	request_num = int(sys.argv[1])
else:
	print("Usage: py " + sys.argv[0] + " <request number> [additional argument]")
	sys.exit(1)

if len(sys.argv) == 3:
	# requests 3,4,5
	additional_arg = sys.argv[2]

# Call request function depending on command line input
if request_num == 1: request1(server_url)
elif request_num == 2: request2(server_url)
elif request_num == 3: 
	if len(additional_arg) > 0 and len(additional_arg) <= max_length:
		request3(server_url, additional_arg)
	else:	
		print("Comment was not the correct length. Aborting.")
		sys.exit(1)
elif request_num == 4: 
	if len(additional_arg) > 0 and len(additional_arg) <= max_length:
		request4(server_url, additional_arg)
	else:	
		print("Quote was not the correct length. Aborting.")
		sys.exit(1)
elif request_num == 5: 

	print("Not yet implemented")


