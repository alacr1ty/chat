#!/usr/bin/env python3

"""
Program: chatserve.py
	Written by: Ava Cordero
	Date: 10/25/2019

Description:
	A simple chat server that works for one pair of users.

"""

import signal
import sys
from socket import *

def server (serverPort):
	sentence = ""


### NEEDS TO BE CHANGED!!!

	# always
	while 1:
		# listen for a connection
		serverSocket = socket (AF_INET,SOCK_STREAM)
		serverSocket.bind (("",serverPort))
		print ("Listening for a connection...")
		serverSocket.listen (1)
		connectionSocket, addr = serverSocket.accept()
		print ("Chat client connected to server on port", serverPort, "...")
		
		# keep connection open until message is "\quit"
		while sentence != "\\quit":
			# receive and decode message
			sentence = connectionSocket.recv (500)
			sentence_str = sentence.decode ("UTF-8")

			# print ("sentence:", sentence_str)

			# send message back to client
			connectionSocket.send (sentence)

		# close connection to client
		connectionSocket.close()


def sig_handle(sig, frame):
	sys.exit(0)



def main ():
	if len(sys.argv) != 2:
		print ("Error: Incorrect usage (chatserve.py serverport).")
		sys.exit(1)
	
	serverPort = int(sys.argv[1])
	# serverSocket = socket (AF_INET,SOCK_STREAM)
	# serverSocket.bind (("",serverPort))
	# serverSocket.listen (1)

	print ("Chat server standing by on port", serverPort, "...")

	server (serverPort)

	
signal.signal(signal.SIGINT, sig_handle)
# signal.pause()

main()