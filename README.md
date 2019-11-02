# Program: quickchat
	Written by: Ava Cordero
	Date: 10/25/2019
	Latest:11/1/2019

# Description:
	A simple chat client/server application that works for one pair of users.

# Usage:
## chatserver
	To start the chat server, use the following, where portnumber is the port on the local machine you want to accept connections from:

$ chatserve.py portnumber

	If the port is open, the server initializes. When the server starts, the user is prompted for a handle with a maximum of 10 characters. It then binds the socket to the port and then begins listening for a connection. Once a client has established a new connection, the chat session begins. Messages can then be exchanged between the client and the server-client, one at a time. If either party enters send message \quit the connection is ended. The server then continues to wait for new connections.

## chatclient
	To open a client connection to the server, use the following, where servername is the hostname of the machine running the server, and portnumber is the server port number to connect to.

$ chatclient.py servername portnumber

	When the client starts, the user is prompted for a handle with a maximum of 10 characters. It then connects to the server at the specified port. Once the client has established a new connection, the chat session begins. Messages can then be exchanged between the client and the server-client, one at a time. If either party enters send message \quit the connection is ended and the client exits.
