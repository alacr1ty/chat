#!/usr/bin/env python3

"""
Program: chatclient.py
	Written by: Ava Cordero
	Date: 10/25/2019
	Latest:11/1/2019

Description:
	A simple chat client that works for one pair of users.

Usage: chatclient.py servername portnumber
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

	# returns a tuple: the socket, and the other handle
	return (clientSocket, handle_server)


def main ():
	# check for proper usage
	if len(sys.argv) != 3:
		print ("Error: Incorrect usage (chatclient.py servername portnumber).")
		exit(1)

	# declare globals cause you're gonna need them
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

	# connects to the server, gets socket and handle
	(clientSocket, handle_server) = conx_user()

	# run the chat client
	run_client (clientSocket, handle_client, handle_server, 0) 


# assign signal handler function
signal.signal(signal.SIGINT, sig_handle)

main()