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

def server (serverSocket):
	while 1:
		connectionSocket, addr = serverSocket.accept()
		sentence = connectionSocket.recv (1024)
		
		capitalizedSentence = sentence.upper().decode ("UTF-8") 
		connectionSocket.send (capitalizedSentence.encode ("UTF-8"))
		
		connectionSocket.close()

def signal_handler(sig, frame):
	sys.exit(0)



def main ():
	if len(sys.argv) != 2:
		print ("error: incorrect usage (chatserve.py serverport).")
		sys.exit(1)

	
	serverPort = int(sys.argv[1])
	serverSocket = socket (AF_INET,SOCK_STREAM)
	serverSocket.bind (("",serverPort))
	serverSocket.listen (1)

	print ("Chat server standing by on port", serverPort, "...")

	server (serverSocket)

	
signal.signal(signal.SIGINT, signal_handler)
# signal.pause()

main()