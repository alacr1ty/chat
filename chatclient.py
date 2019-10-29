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
from chatlib import config_user



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

# connects the client to the server and maintains the chat functionality
def run_client (clientSocket, handle):
	prompt = handle+">"

	# continuously prompt for a message until the message is "\quit"
	msg = ""
	while 1:
		msg = message (prompt, clientSocket, 500)
		if msg == "\\quit": # if message is "\quit", 
			print ("Connection closed...")
			exit(0)



def main ():
	# check for proper usage
	if len(sys.argv) != 3:
		print ("Error: Incorrect usage (chatclient.py serverport).")
		exit(1)

	# assign host and port from args
	serverName = sys.argv[1]
	serverPort = int (sys.argv[2])

	print ("Chat client starting ...")

	# gets user handle
	handle_client = config_user()

# try:
	# connect to the server
	clientSocket = socket (AF_INET, SOCK_STREAM) # create TCP socket
	clientSocket.connect ((serverName,serverPort)) # connect to server

	clientSocket.send(handle_client.encode ("UTF-8")) # send handle to server
	handle_server = clientSocket.recv (10).decode ("UTF-8")

	print ("Chat client connected to '" + handle_server + "' on server '" + serverName + "' on port " + str(serverPort) + "...")
# except:
# 	print ("Could not connect to server", serverName, "on port", serverPort, "...")
# 	exit(1)

	run_client(clientSocket, handle_client) # run client

main()