#!/usr/bin/env python3

"""
Program: chatserve.py
	Written by: Ava Cordero
	Date: 10/25/2019
	Latest: 11/1/2019

Description:
	A simple chat server that works for one pair of users.

"""

# imports
import signal
import sys
from socket import *
from chatlib import *

# starts and maintains the server functionality
def start_server (server_port, server_socket):
	# sentence = ""

	handle_server = config_user()

	# always
	while 1:
		# listen for a connection
		print ("Listening for a connection on port " + str(server_port) + "...")
		server_socket.listen (1) # wait for an incoming connection
		connectionSocket, addr = server_socket.accept() # accept and get socket info
		
		handle_client = connectionSocket.recv (10).decode ("UTF-8") # get the incoming user handle
		connectionSocket.send (handle_server.encode ("UTF-8")) # send the local user handle

		print ("Chat client '" + handle_client + "' connected to server on port " + str(server_port) + "...")
		
		# keep connection open until message is "\quit"
		stop = 0
		while stop is 0:

			stop = run_client_srv (connectionSocket, handle_server, handle_client) # run the server-based client


# main function
def main ():
	# check that usage is correct
	if len(sys.argv) != 2:
		print ("Error: Incorrect usage (chatserve.py serverport).")
		sys.exit(1)
	
	# assign server port and socket
	server_port = int(sys.argv[1]) # port comes from args
	server_socket = socket (AF_INET,SOCK_STREAM) # create socket
	server_socket.bind (("",server_port)) # bind socket to port

	print ("Chat server starting ...")

	start_server (server_port, server_socket) # start server


# assign signal handler function
signal.signal(signal.SIGINT, sig_handle)

main()