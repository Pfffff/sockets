import os
import socket

sock = socket.socket()

sock.bind(('localhost', 8000))

sock.listen(1)

print ('Listen...')

while True:


	conn, addr = sock.accept()
        print("New connection from " + addr[0])

	data = conn.recv(1024)
	
	udata = data.decode("utf-8")
  
	udata = udata.split("\r\n", 1)[0]
	
	method, address, protocol = udata.split(" ")
	
        if address == "/index.html" or address == "/":
		
		if os.path.exists("./index.html"):
			
			file = open ("./index.html", "rb")
			conn.send("""HTTP/1.1 200 OK \n Content type:text HTML\n\n\n """ + file.read())
			file.close()
	elif address == "about/aboutme.html":
		print("aboutme!")
		if os.path.exists("./" + address):
			file = open ("." + address, "rb")
			conn.send("""HTTP 200 OK \n Content type:text HTML\n\n\n """ + file.read())	
			file.close()
	conn.close()
sock.close()
	




			
		


