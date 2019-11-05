#!/usr/bin/env python3

"""
Program: chatclient.py
	Written by: Ava Cordero
	Date: 10/25/2019
	Latest: 11/5/2019

Description:
	Library for a simple chat client that works for one pair of users.

"""

# imports
import sys
from socket import *



#Function: config_user (Configure user)
#Description: Configures user handle for messaging system.
#Input: Maximum character length of the handle.
#Output: User handle.
def config_user (max_len):
	handle = ""
	
	handle = input ("Enter handle (max 10 chars): ")

	# prompt user for a handle no longer than 10 chars
	while len(handle) > max_len or len(handle) == 0:
		handle = input ("Enter handle: ")
		if len(handle) > max_len:
			print ("Exceeded maximum characters allowed (10), try again.")
	
	return handle

#Function: recv_message (Receive message)
#Description: Recceives a chat message from the other user.
#Input: Socket, prompt, and maximum character length for the message.
#Output: String including prompt and message.
def recv_message (socket, prompt, message_max):
	# receive the message back from server
	sentence = socket.recv (message_max).decode ("UTF-8")

	return (prompt + sentence) # must be UTF-8

#Function: send_message (Send message)
#Description: Prompts for and sends a chat message to the other user.
#Input: Socket, prompt, and maximum character length for the message.
#Output: String including message.
def send_message (socket, prompt, message_max):
	sentence = ""

	# prompt user for a message that is no longer than the maximum
	while len(sentence) > message_max or len(sentence) == 0:
		sentence = input (prompt)
		if len(sentence) > message_max:
			print ("Exceeded maximum characters allowed (" +
				str(message_max) + "), try again.")

	socket.send (sentence.encode ("UTF-8")) # send the message

	return (sentence) # must be UTF-8


# signal handler function
def sig_handle(sig, frame):
	sys.exit(0)
