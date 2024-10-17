from jinja2 import Environment, FileSystemLoader
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            response = self.home()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(response.encode('utf-8'))

    def render_response_from_env(self, env):
        # Simulate getting the name parameter from the user request
        name = self.get_name_parameter()
        
        # Get the template from the environment
        template = env.get_template('template.html')
        
        # Render the template with the name parameter
        rendered_template = template.render(name=name)
        
        return rendered_template

    def home(self):
        env = Environment(loader=FileSystemLoader('templates'))
        response = self.render_response_from_env(env)
        return response

    def get_name_parameter(self):
        # Replace this method with actual user input retrieval logic
        return 'World'

def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()