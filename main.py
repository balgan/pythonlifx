import socket
import time
sock = socket.socket()
sock.connect(("192.168.1.101",56700))
#p = purple
#r = red
#w = bright white
p = '31000034000000000000000000000000d073d500a1bf00000000000000000000660000000015ccfffff401000000000000'.decode('hex')
r = '31000034000000000000000000000000d073d500a1bf0000000000000000000066000000000000ffffe803000000000000'.decode('hex')
w = '31000034000000000000000000000000d073d500a1bf000000000000000000006600000000000000000080f00a13050000'.decode('hex')
lighton = '26000034000000000000000000000000d073d500a1bf00000000000000000000150000000001'.decode('hex')
lightoff = '26000034000000000000000000000000d073d500a1bf00000000000000000000150000000000'.decode('hex')

def main():

	print "q for on\n"
	print "w for off\n"
	print "e for purple\n"
	print "r for red\n"
	print "t for white\n"

	while(True):
		option = raw_input("which option? \n")
		if option.strip() == 'q':
			sock.send(lighton)
		if option.strip() == 'w':
			sock.send(lightoff)
	        if option.strip() == 'e':
        	        sock.send(p)
	        if option.strip() == 'r':
        	        sock.send(r)
	        if option.strip() == 't':
        	        sock.send(w)


main()
