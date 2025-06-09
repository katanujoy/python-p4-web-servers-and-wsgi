from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

def application(environ, start_response):
    request = Request(environ)
    print(f'This web server is running at {request.remote_addr}')
    response = Response('A WSGI generated this response!')
    return response(environ, start_response)

if __name__ == '__main__':
    run_simple(
        hostname='localhost',
        port=5555,
        application=application
    )
