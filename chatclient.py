#!/usr/bin/env python3

"""
Program: chatclient.py
	Written by: Ava Cordero
	Date: 10/25/2019

Description:
	A simple chat client that works for one pair of users.

"""



import sys
from socket import *



def client (clientSocket):
	sentence = input ("Input lowercase sentence:")
	clientSocket.send (sentence.encode ("UTF-8"))

	modifiedSentence = clientSocket.recv (1024)
	print ("From Server:", modifiedSentence.decode ("UTF-8"))

	clientSocket.close()

def main ():
	print (sys.argv)

	if len(sys.argv) != 3:
		print ("error: incorrect usage (chatclient.py serverport).")
		exit(1)

	serverName = sys.argv[1]
	serverPort = int(sys.argv[2])

	clientSocket = socket (AF_INET, SOCK_STREAM)
	clientSocket.connect ((serverName,serverPort))

	client(clientSocket)

main()