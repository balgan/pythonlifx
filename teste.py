import socket
import struct
import time
sock = socket.socket()
sock.connect(("192.168.1.101",56700))
lighton = '26000034000000000000000000000000d073d500a1bf00000000000000000000150000000001'.decode('hex')
lightoff = '26000034000000000000000000000000d073d500a1bf00000000000000000000150000000000'.decode('hex')

while(True):
	sock.send(lightoff)
	time.sleep(1)
	sock.send(lighton)
	time.sleep(1)
