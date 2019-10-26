#!/usr/bin/env python3

"""
Program: chatclient.py
	Written by: Ava Cordero
	Date: 10/25/2019

Description:
	A simple chat client that works for one pair of users.

"""

# imports
import sys
from socket import *



# connects the client to the server
def run_server (clientSocket):
	# variables
	msg = ""

	# gets user handle and configs prompt
	handle = message ("Enter handle: ", clientSocket)
	prompt = (handle + "> ")

	# continuously prompt for a message until the message is "\quit"
	while msg != "\\quit":
		msg = message (prompt, clientSocket)
		# print ("msg:", msg)

	clientSocket.close()

def message (message, clientSocket):
	sentence = input (message)
	
	clientSocket.send (sentence.encode ("UTF-8"))
	message = clientSocket.recv (1024)

	return (message.decode ("UTF-8"))

def main ():
	if len(sys.argv) != 3:
		print ("Error: Incorrect usage (chatclient.py serverport).")
		exit(1)

	serverName = sys.argv[1]
	serverPort = int (sys.argv[2])

	clientSocket = socket (AF_INET, SOCK_STREAM)
	clientSocket.connect ((serverName,serverPort))

	run_server(clientSocket)

main()