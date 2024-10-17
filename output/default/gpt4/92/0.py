from jinja2 import Environment, FileSystemLoader

def render_response_from_env(env, request):
    name = request.get('name')
    template = env.get_template('template.html')  # replace with your template name
    rendered_template = template.render(name=name)
    return {
        'status': '200 OK',
        'body': rendered_template
    }

def home(env, request):
    response = render_response_from_env(env, request)
    return response

# Example usage
if __name__ == "__main__":
    env = Environment(loader=FileSystemLoader('templates'))  # specify your templates directory
    request = {'name': 'John Doe'}
    response = home(env, request)
    print(response)