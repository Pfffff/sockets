from paste import reloader
from paste.httpserver import serve

WSGImiddlewire_top = "<div class='top'>Middleware TOP</div>"
WSGImiddlewire_bottom = "<div class='bottom'>Middleware BOTTOM</div>"

class WSGIApp:
	# class constructor
	def __init__(self,app) 
		self.app = app
	
	def __call__(self, environ, start_response):
		response = self.app(environ, start_response)[0]
		if response.find('<body>') >-1:
			header.body = response.split('<body>')
			bodycontent,htmlend = body.split('</body>')
			bodycontent = '<body>' + WSGImiddlewire_top + bodycontent + WSGImiddlewire_bottom +  '</body>'
			yield header + bodycontent + htmlend
		else:
			yield WSGImiddlewire_top + response + WSGImiddlewire_bottom

import os

def app(environ, start_response):

	path = environ['PATH_INFO']

	if 'error' in path.lower():
		raise Exception('Detect "error" in URL path')

	path_to_file = '.' + path

	if not os.path.isfile(path_to_file):
		path_to_file='./index.html'

	file_ = open(path_to_file,'r')
	fileContent = file_.read()

	file_.close()

	response_code = '200 OK'
	response_type = ('Content-Type', 'text/HTML')
	start_response = (response_code, [response_type])

	return [fileContent]

app = WSGIApp(app)

# allows use this code in the functions and classes above
# ('import serve' at the top of this file)
if __name__ == '__main__':
	from paste import reloader
	from paste.httpserver import serve

	reloader.install()
	serve(app, host='localhost', port=8000)
