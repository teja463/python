
# Client Module
import socket

def Main(host, port):
    
	# Creates a socket object representing client
    clientObj = socket.socket()

	# Connec to that host and port
    clientObj.connect((host,port))

	# Take input from user to send it across to the server
    req = input("Enter request: ")

    while (req !="bye"):

		# Encode the text entered by the user and send it to the server
        clientObj.send(req.encode('utf-8'))

		# Recieve the response from the server and decode bytest to string
        res = clientObj.recv(1024).decode('utf-8')

		# Print the response to the console
        print ("Server says: ", res)

		# Take input from the user
        req = input("Enter request: ")
    
    clientObj.close()

Main ('127.0.0.1', 5000)
