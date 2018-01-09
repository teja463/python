
# Server Module

import socket


def Main(host, port):

	# Creates socket object 
    socketObj = socket.socket()

	# Bind the objec to that host and port
    socketObj.bind((host,port))

	# Listen for the client connection
    socketObj.listen(1)

	# Accept messages from the client
    conn, addr = socketObj.accept()

    print ("Client connected from %s" %(str(addr)))

    while(True):
	
		# Recive the message from client and decode it from byts to string
        req = conn.recv(1024).decode('utf-8')
        if not req:
            break

        print ("Client says: ", req)

        res = input("Enter response: ")

		# Send response to the clinet
        conn.send(res.encode('utf-8'))
        
	# Close the connection
    conn.close()

Main('127.0.0.1',5000)
        
