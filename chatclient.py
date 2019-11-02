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


def conx_user(): # (server_name, server_port, handle_client):
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


def main ():
	# check for proper usage
	if len(sys.argv) != 3:
		print ("Error: Incorrect usage (chatclient.py servername portnumber).")
		exit(1)

	# declare globals cause you're gonna need them
	global server_name
	global server_port
	global client_socket
	global handle_server
	global handle_client

	# assign host and port from args
	server_name = sys.argv[1]
	server_port = int (sys.argv[2])

	print ("Chat client starting ...")

	# gets client user handle
	handle_client = config_user()

	# connects to the server, gets socket and handle
	(client_socket, handle_server) = conx_user()

	# run the chat client
	run_client (client_socket, handle_client, handle_server, 0) 


# assign signal handler function
signal.signal(signal.SIGINT, sig_handle)

main()