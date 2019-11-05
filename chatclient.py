#!/usr/bin/env python3

"""
Program: chatclient.py
	Written by: Ava Cordero
	Date: 10/25/2019
	Latest:11/5/2019

Description:
	A simple chat client that works for one pair of users.
	See chatlib.py for utility functions.

Usage: chatclient.py servername portnumber
"""

# imports
import signal
import sys
from socket import *
from chatlib import *

#Function: conx_user (Connect user)
#Description: Connects the client to the server.
#Input: Server name and port to which to connect
#Output: Tuple containing the client socket and server handle.
def conx_user (server_name, server_port, handle_client):
# try:
	# connect to the server
	client_socket = socket (AF_INET, SOCK_STREAM) # create TCP socket
	client_socket.connect ((server_name,server_port)) # connect to server

	# servers share handles
	client_socket.send(handle_client.encode ("UTF-8")) 
	handle_server = client_socket.recv (10).decode ("UTF-8")

	print ("Chat client connected to '" + handle_server + "' on server '" + server_name + "' on port " + str(server_port) + "...")

	# returns a tuple: the socket, and the other handle
	return (client_socket, handle_server)

#Function: run_client (Run client)
#Description: Runs and maintains the client functionality.
#Input: Client socket, client handle, and server handle.
#Output: None.
# maintains the client chat functionality
def run_client (client_socket, handle_cl, handle_srv):
	# set prompts
	prompt_srv = handle_srv + "> "
	prompt_cl = handle_cl + "> "

	# continuously prompt for a message until the message is "\quit"
	while 1:
		msg_out = send_message (client_socket, prompt_cl, 500)
		msg_in = recv_message (client_socket, prompt_srv, 500)
		print (msg_in)
		
		if msg_out == "\\quit": # if message is "\quit", 
			print ("Connection closed...")
			exit(0)

		if msg_in == prompt_srv + "\\quit": # if message is "\quit", 
			print ("Connection closed by '" + handle_srv + "'...")
			exit(0)



# Function: Main
# Description: Validates arguments, then calls functions to configure the user, connect to the server, and run the chat client.
# Input: Command line arguments.
# Output: None.
def main ():
	# check for proper usage
	if len(sys.argv) != 3:
		print ("Error: Incorrect usage (chatclient.py servername portnumber).")
		exit(1)

	# assign host and port from args
	server_name = sys.argv[1]
	server_port = int (sys.argv[2])

	print ("Chat client starting ...")

	# configure user handle w/ max 10 chars
	handle_client = config_user(10)

	# connect to the server, get socket and handle
	(client_socket, handle_server) = conx_user (server_name, server_port, handle_client)

	# run the chat client
	run_client (client_socket, handle_client, handle_server) 


# assign signal handler function
signal.signal(signal.SIGINT, sig_handle)

main()