from jinja2 import FileSystemLoader, Environment
from wsgiref.simple_server import make_server

def application(environ, start_response):
    env = Environment(loader=FileSystemLoader("pytho_test_in_git/templates"))
    template = env.get_template('template.html')

    data = {
        'title': 'WSGI tutorial',
        'username': 'Codi'
    }

    html = template.render(data)

    headers = [ ('Content-type', 'text/html; charset=utf-8') ]

    start_response('200 OK', headers)

    return [bytes(html, 'utf-8')]

server = make_server('localhost', 5583, application)
server.serve_forever()