#!/usr/bin/env python3

"""
Program: chatserve.py
	Written by: Ava Cordero
	Date: 10/25/2019
	Latest: 11/5/2019

Description:
	A simple chat server that works for one pair of users.

"""

# imports
import signal
import sys
from socket import *
from chatlib import *



#Function: run_client_srv (Run server-side client)
#Description: Maintains the server-side chat functionality.
#Input: Connection socket, server handle, and client handle.
#Output: Returns 1 to start_srv to end the connection.
def run_client_srv (connection_socket, handle_srv, handle_cl):
	# set prompts
	prompt_srv = handle_srv + "> "
	prompt_cl = handle_cl + "> "

	# keep prompting until the message is "\quit"
	while 1:
		msg_in = recv_message (connection_socket, prompt_cl, 500)
		print (msg_in)
		if msg_in == prompt_cl + "\\quit": # if message is "\quit"
		 	# close connection to client
			print ("Connection closing...")
			connection_socket.close() # close connection
			print ("Connection closed by '" + handle_cl + "'...")
			return 1
		msg_out = send_message (connection_socket, prompt_srv, 500)
		if msg_out == "\\quit": # if message is "\quit"
		 	# close connection to client
			print ("Connection closing...")
			connection_socket.close() # close connection
			print ("Connection to '" + handle_cl + "' closed...")
			return 1

#Function: start_srv (Start server)
#Description: Starts and maintains the server functionality. Calls the run_client_srv function when a connection is established.
#Input: Port and socket on which to run the server, and server handle.
#Output: None.
def start_srv (server_port, server_socket, handle_srv):
	# always
	while 1:
		# listen for a connection
		print ("Listening for a connection on port " + str(server_port) + "...")
		server_socket.listen (1) # wait for an incoming connection
		connection_socket, addr = server_socket.accept() # accept and get socket info
		
		handle_client = connection_socket.recv (10).decode ("UTF-8") # get the incoming user handle
		connection_socket.send (handle_srv.encode ("UTF-8")) # send the local user handle

		print ("Chat client '" + handle_client + "' connected to server on port " + str(server_port) + "...")
		
		# keep connection open until message is "\quit"
		stop = 0
		while stop is 0:

			# run the server-based client until stop is returned
			stop = run_client_srv (connection_socket, handle_srv, handle_client)


#Function: Main
#Description:Validates arguments, then calls functions to set up the socket, configure the user, and start the server.
#Input: Command line arguments.
#Output: None.
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

	#configure user handle w/ max 10 chars
	handle_server = config_user(10)

	# start server
	start_srv (server_port, server_socket, handle_server)


# assign signal handler function
signal.signal(signal.SIGINT, sig_handle)

main()