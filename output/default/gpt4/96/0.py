from wsgiref.simple_server import make_server

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    return [b'Hello, World!']

if __name__ == '__main__':
    server = make_server('localhost', 8000, application)
    print("Serving on http://localhost:8000")
    server.serve_forever()