import socket


def answer(socket):
	answer_data = ""
	current_data = socket.recv(4096)
	while current_data:
		answer_data = answer_data + current_data
		current_data = socket.recv(4096)


wikipedia_request = """GET /wiki/Main_Page HTTP/1.1\r\n
Host: en.wikipedia.org\r\n
User-Agent: Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509\r\n
Firefox/3.0b5\r\n
Accept: text/html\r\n
Connection: close\r\n\r\n\r\n
"""

htttpbin_requests = [
"""GET /ip HTTP/1.1\r\n
Host: httpbin.org\r\n
Accept: */*\r\n""",
 
"""GET /get?foo=bar&1=2&2/0&error=True HTTP/1.1\r\n
Host: httpbin.org\r\n
Accept: */*\r\n""",
 
"""POST /post HTTP/1.1\r\n
Host: httpbin.org\r\n
Accept: */*\r\n
Content-Length: 35\r\n
Content-Type: application/x-www-form-urlencoded\r\n
\r\n
\r\n
\r\n
foo=bar&1=2&2%2F0=&error=True\r\n
"""
,
"""GET /cookies/set?country=Ru HTTP/1.1\r\n
Host: httpbin.org\r\n
Accept: */*\r\n"""
,
 
"""GET /cookies HTTP/1.1\r\n
Host: httpbin.org\r\n
Accept: */*\r\n"""
,
"""GET /redirect/4 HTTP/1.1\r\n
Host: httpbin.org\r\n
Accept: */*\r\n"""

"""GET /redirect/4 HTTP/1.1\r\n
Host: httpbin.org\r\n
Accept: */*\r\n"""
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









