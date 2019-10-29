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
from chatlib import *





def main ():
	# check for proper usage
	if len(sys.argv) != 3:
		print ("Error: Incorrect usage (chatclient.py serverport).")
		exit(1)

	# assign host and port from args
	serverName = sys.argv[1]
	serverPort = int (sys.argv[2])

	print ("Chat client starting ...")

	# gets client user handle
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

	run_client (clientSocket, handle_client, handle_server) # run client

main()