from wsgiref.simple_server import make_server

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return [b'Hello, World!']

if __name__ == '__main__':
    with make_server('', 8000, application) as server:
        print("Serving on port 8000...")
        server.serve_forever()