#!/usr/bin/env python3

"""
Program: chatclient.py
	Written by: Ava Cordero
	Date: 10/25/2019

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