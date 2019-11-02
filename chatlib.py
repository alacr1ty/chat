#!/usr/bin/env python3

"""
Program: chatclient.py
	Written by: Ava Cordero
	Date: 10/25/2019
	Latest: 11/1/2019

Description:
	Library for a simple chat client that works for one pair of users.

"""

# imports
import sys
from socket import *



# configures handle for messaging system
def config_user ():
	handle = ""
	
	handle = input ("Enter handle (max 10 chars): ")

	# prompt user for a handle no longer than 10 chars
	while len(handle) > 10 or len(handle) == 0:
		handle = input ("Enter handle: ")
		if len(handle) > 10:
			print ("Exceeded maximum characters allowed (10), try again.")
	
	return handle

# prompt user for message, then send and recv to/from server
def recv_message (client_socket, prompt):
	# receive the message back from server
	sentence = client_socket.recv (1024).decode ("UTF-8")

	return (prompt + sentence) # must be UTF-8

# maintains the client chat functionality
def run_client (client_socket, handle_cl, handle_srv, is_srv):
	# set prompts
	prompt_srv = handle_srv + "> "
	prompt_cl = handle_cl + "> "

	# continuously prompt for a message until the message is "\quit"
	while 1:
		msg = send_message (client_socket, prompt_cl, 500)
		
		if msg == "\\quit": # if message is "\quit", 
			print ("Connection closed...")
			exit(0)
		
		msg = recv_message (client_socket, prompt_srv)
		print (msg)

		if msg == prompt_srv + "\\quit": # if message is "\quit", 
			print ("Connection closed...")
			exit(0)

# maintains the server-side chat functionality
def run_client_srv (connection_socket, handle_srv, handle_cl):
	# set prompts
	prompt_srv = handle_srv + "> "
	prompt_cl = handle_cl + "> "

	# keep prompting until the message is "\quit"
	while 1:
		msg = recv_message (connection_socket, prompt_cl)
		print (msg)
		if msg == prompt_cl + "\\quit": # if message is "\quit"
		 	# close connection to client
			print ("Connection closing...")
			connection_socket.close() # close connection
			print ("Connection closed...")
			return 1
		msg = send_message (connection_socket, prompt_srv, 500)
		if msg == "\\quit": # if message is "\quit"
		 	# close connection to client
			print ("Connection closing...")
			connection_socket.close() # close connection
			print ("Connection closed...")
			return 1

# prompt user for message, then send and recv to/from server
def send_message (client_socket, prompt, message_max):
	sentence = ""

	# prompt user for a message that is no longer than the maximum
	while len(sentence) > message_max or len(sentence) == 0:
		sentence = input (prompt)
		if len(sentence) > message_max:
			print ("Exceeded maximum characters allowed (" +
				str(message_max) + "), try again.")

	client_socket.send (sentence.encode ("UTF-8")) # send the message
	# prompt = client_socket.recv (1024) # receive the message back from server

	return (sentence) # must be UTF-8


# signal handler function
def sig_handle(sig, frame):
	sys.exit(0)
