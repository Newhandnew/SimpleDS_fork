## #!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
import socket
import sys
import os
from time import sleep
from  open_youtube import call_letitgo


HOST, PORT = "localhost", 2015

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(0.5)
timeout = 0
r = sr.Recognizer()
speech_command = 'google_speech -l en '

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
						print "split:", received.split('\x00')
						for response in received.split('\x00'):
							if response.find('"') != -1:
								response = response[response.find('"'):]	# because server would return strange char
								command = speech_command + response
								print command
								os.system(command)
								if response.find('banana') != -1:
									call_letitgo()

			except:
				pass
			with sr.Microphone() as source:
				audio = r.listen(source)
				data = ""

			try:
    			# for testing purposes, we're just using the default API key
    			# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    			# instead of `r.recognize_google(audio)`
    				data = r.recognize_google(audio)
				print("You said: " + data)
			except sr.UnknownValueError:
				print("Google Speech Recognition could not understand audio")
			except sr.RequestError as e:
    				print("Could not request results from Google Speech Recognition service; {0}".format(e))

			# data = raw_input ( "SEND( TYPE q or Q to Quit):" )
			if (data <> 'Q' and data <> 'q'):
				sock.send(data)
			else:
				sock.send(data)
				sock.close()
				break
