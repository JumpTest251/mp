from jinja2 import Environment, FileSystemLoader
from wsgiref.simple_server import make_server

def render_response_from_env(env):
    # Get the name parameter from the request
    name = env['QUERY_STRING'].split('name=')[-1] if 'name=' in env['QUERY_STRING'] else 'World'
    
    # Get the template from the environment
    template = env['template_loader'].get_template('template.html')
    
    # Render the template with the name parameter
    rendered_template = template.render(name=name)
    
    # Return a response with the rendered template
    return '200 OK', [('Content-Type', 'text/html')], [rendered_template.encode('utf-8')]

def home(env, start_response):
    # Call the render_response_from_env function with the env variable
    status, headers, body = render_response_from_env(env)
    start_response(status, headers)
    return body

# Sample WSGI app setup
def app(environ, start_response):
    return home(environ, start_response)

if __name__ == '__main__':
    # Setup the Jinja2 environment
    template_loader = FileSystemLoader('.')
    environment = Environment(loader=template_loader)
    
    # Add template loader to the environment
    env = {
        'QUERY_STRING': '',
        'template_loader': environment,
    }
    
    # Start the server
    server = make_server('localhost', 8080, app)
    print("Serving on http://localhost:8080...")
    server.serve_forever()