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



# connects the client to the server and maintains the chat functionality
def run_client (clientSocket):
	# variables
	msg = ""

	# gets user handle and configs prompt
	handle = message ("Enter handle: ", clientSocket, 10)
	prompt = (handle + "> ")

	# continuously prompt for a message until the message is "\quit"
	while 1:
		msg = loc_msg = message (prompt, clientSocket, 500)
		if loc_msg == "\\quit": # if message is "\quit", close the connection
			print ("Connection closing...")
			clientSocket.close() # close the connection
			print ("Connection closed...")
			exit(0)

# prompt user for message, then send and recv to/from server
def message (prompt, clientSocket, message_max):
	sentence = ""

	# prompt user for a message that is no longer than the maximum
	while len(sentence) > message_max or len(sentence) == 0:
		sentence = input (prompt)
		if len(sentence) > message_max:
			print ("Exceeded maximum characters allowed (" +
				str(message_max) + "), try again.")

	clientSocket.send (sentence.encode ("UTF-8")) # send the message
	prompt = clientSocket.recv (1024) # receive the message back from server

	return (prompt.decode ("UTF-8")) # must be UTF-8


def main ():
	# check for proper usage
	if len(sys.argv) != 3:
		print ("Error: Incorrect usage (chatclient.py serverport).")
		exit(1)

	# assign host and port from args
	serverName = sys.argv[1]
	serverPort = int (sys.argv[2])

	# connect to the server
	clientSocket = socket (AF_INET, SOCK_STREAM) # create TCP socket
	clientSocket.connect ((serverName,serverPort)) # connect to server

	run_client(clientSocket) # run client

main()