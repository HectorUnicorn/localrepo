import socket
HOST='127.0.0.1'
PORT=20000
BUFFER=4*1024
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((HOST,PORT))
socket.listen(0)
print('tcpServer listen at: %s:%s\n\r' %(HOST,PORT))
while True:
	client_sock,client_addr=socket.accept()
	print('%s:%s connect' %client_addr)
	while True:
		recv=client_sock.recv(BUFFER)
		if not recv:
			client_sock.close()
			break;
		print('[Client %s:%s said]:%s' % (client_addr[0],client_addr[1],recv))
		client_sock.send('tcpServer has received your message')
sock.close()