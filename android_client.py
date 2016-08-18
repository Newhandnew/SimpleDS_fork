#client example
import socket
import sys
from time import sleep

HOST, PORT = "localhost", 2015

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)
timeout = 0
while(timeout<3):
	try:
		# Connect to server and send data
		sock.connect((HOST, PORT))
		# Receive data from the server and shut down
	except:
		timeout += 1
		sleep(1)
		pass
	finally:
		timeout = 3
		while 1:
			try:
				while 1:
					received = sock.recv(1024)
					if received != "":
						print "RECIEVED:" , received
			except:
				pass
			data = raw_input ( "SEND( TYPE q or Q to Quit):" )
			if (data <> 'Q' and data <> 'q'):
				sock.send(data)
			else:
				sock.send(data)
				sock.close()
				break

