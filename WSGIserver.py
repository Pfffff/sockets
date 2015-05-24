from paste import reloader
from paste.httpserver import serve

TOP = "<div class='top'>Middleware TOP</div>"
BOTTOM = "<div class='botton'>Middleware BOTTOM</div>"

class WSGIApp(object):
	def __init__(self, app):
		self.app = app
	def __call__(self, environ, start_response):
		response = self.app(environ, start_response)[0]
		if response.find('<body>') >-1:
			header,body = response.split('<body>')
			data,htmlend = body.split('</body>')
			data = '<body>'+ TOP + data + BOTTOM+'</body>'
			yield header + data + htmlend
		else:
			yield TOP + response + BOTTOM

import os

def app(environ, start_response):

	path = environ['PATH_INFO']
	filePath = '.' + path
	if not os.path.isfile(filePath):
		filePath ='./index.html'
	file_ = open(filePath,'r')
	fileContent = file_.read()
	file_.close()

	response_code = '200 OK'
	response_type = ('Content-Type', 'text/HTML')
	start_response(response_code, [response_type])
	return [fileContent ]

app = WSGIApp(app)


# allows use this code in the functions and classes above
# ('import serve' at the top of this file)
if __name__ == '__main__':
	from paste import reloader
	from paste.httpserver import serve

	reloader.install()
	serve(app, host='localhost', port=8000)
