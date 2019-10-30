#!/usr/bin/env python3

"""
Program: chatclient.py
	Written by: Ava Cordero
	Date: 10/25/2019

Description:
	A simple chat client that works for one pair of users.

"""

# imports
import signal
import sys
from socket import *

from chatlib import *


def conx_user(): # (serverName, serverPort, handle_client):
# try:
	# connect to the server
	clientSocket = socket (AF_INET, SOCK_STREAM) # create TCP socket
	clientSocket.connect ((serverName,serverPort)) # connect to server

	# servers share handles
	clientSocket.send(handle_client.encode ("UTF-8")) 
	handle_server = clientSocket.recv (10).decode ("UTF-8")

	print ("Chat client connected to '" + handle_server + "' on server '" + serverName + "' on port " + str(serverPort) + "...")

	return (clientSocket, handle_server)

def main ():
	# check for proper usage
	if len(sys.argv) != 3:
		print ("Error: Incorrect usage (chatclient.py serverport).")
		exit(1)

	global serverName
	global serverPort
	global clientSocket
	global handle_server
	global handle_client

	# assign host and port from args
	serverName = sys.argv[1]
	serverPort = int (sys.argv[2])

	print ("Chat client starting ...")

	# gets client user handle
	handle_client = config_user()

	# connects to the server, sets 
	(clientSocket, handle_server) = conx_user()

	# run the chat client
	run_client (clientSocket, handle_client, handle_server, 0) 


# assign signal handler function
signal.signal(signal.SIGINT, sig_handle)

main()