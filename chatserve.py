#!/usr/bin/env python3

"""
Program: chatserve.py
	Written by: Ava Cordero
	Date: 10/25/2019

Description:
	A simple chat server that works for one pair of users.

"""

# imports
import signal
import sys
from socket import *

from chatlib import *

# starts and maintains the server functionality
def start_server (serverPort, serverSocket):
	# sentence = ""

	handle_server = config_user()

	# always
	while 1:
		# listen for a connection
		print ("Listening for a connection on port " + str(serverPort) + "...")
		serverSocket.listen (1)
		connectionSocket, addr = serverSocket.accept()
		
		handle_client = connectionSocket.recv (10).decode ("UTF-8")
		connectionSocket.send (handle_server.encode ("UTF-8"))

		print ("Chat client '" + handle_client + "' connected to server on port " + str(serverPort) + "...")
		
		# keep connection open until message is "\quit"
		stop = 0
		while stop is 0:

			stop = run_client_srv (connectionSocket, handle_server, handle_client)
			# if stop is 1:
			# 	break

			# run_client (connectionSocket, handle_server, handle_client, 1)
			



# main function
def main ():
	# check that usage is correct
	if len(sys.argv) != 2:
		print ("Error: Incorrect usage (chatserve.py serverport).")
		sys.exit(1)
	
	# assign server port and socket
	serverPort = int(sys.argv[1]) # port comes from args
	serverSocket = socket (AF_INET,SOCK_STREAM) # create socket
	serverSocket.bind (("",serverPort)) # bind socket to port

	print ("Chat server starting ...")

	start_server (serverPort, serverSocket) # start server


# assign signal handler function
signal.signal(signal.SIGINT, sig_handle)

main()