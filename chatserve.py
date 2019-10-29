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
from chatlib import config_user

# starts and maintains the server functionality
def start_server (serverPort, serverSocket):
	# sentence = ""

	handle = config_user()

	# always
	while 1:
		# listen for a connection
		print ("Listening for a connection on port", serverPort, "...")
		serverSocket.listen (1)
		connectionSocket, addr = serverSocket.accept()
		print ("Chat client connected to server on port", serverPort, "...")
		
		# keep connection open until message is "\quit"
		while 1:
			
			# receive and decode message
			sentence = connectionSocket.recv (1024)
			sentence_str = sentence.decode ("UTF-8")

			# print ("sentence:", sentence_str)

			# send message back to client
			connectionSocket.send (sentence)

			if sentence_str == "\\quit":
				# close connection to client
				print ("Connection closing...")
				connectionSocket.close() # close connection
				print ("Connection closed...")
				break

# signal handler function
def sig_handle(sig, frame):
	sys.exit(0)


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