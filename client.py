import socket


def answer(socket):
	answer_data = ""
	current_data = socket.recv(4096)
	while current_data:
		answer_data = answer_data + current_data
		current_data = socket.recv(4096)


wikipedia_request = """GET /wiki/страница HTTP/1.1
Host: ru.wikipedia.org
User-Agent: Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509
Firefox/3.0b5
Accept: text/html
Connection: close 

"""

htttpbin_requests = [
"""GET /ip HTTP/1.1
Host: httpbin.org
Accept: */* 

""",

"""GET /get?foo=bar&1=2&2/0&error=True HTTP/1.1
Host: httpbin.org
Accept: */* 

""",

"""POST /post HTTP/1.1
Host: httpbin.org
Accept: */*
Content-Length: 35
Content-Type: application/x-www-form-urlencoded
 
foo=bar&1=2&2%2F0=&error=True 

""",

"""GET /cookies/set?country=Ru HTTP/1.1
Host: httpbin.org
Accept: */* 

""",

"""GET /cookies HTTP/1.1
Host: httpbin.org
Accept: */* 

""",

"""GET /redirect/4 HTTP/1.1
Host: httpbin.org
Accept: */* 

"""
]





client = socket.socket()

client.connect(("wikipedia.org",80))
client.send(wikipedia_request)
data = answer(client)
client.close()
new_file = open("wikipedia.html",'w')
new_file.write(data)
new_file.close()


for request in httpbin_requests:
	client = socket.socket()
	client.connect((HTTPBIN,80))
	client.send(request)
	data =answer(client)
	client.close()
	httpbin_file = open("httpbin"+httpbin_requests.index(request)+".html",'w')
	httpbin_file.write(data)
	httpbin_file.close()









