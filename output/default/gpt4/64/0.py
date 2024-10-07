from jinja2 import Environment, select_autoescape

def render_response_from_env(env, request):
    name = request.get('name', 'World')  # Default to 'World' if no name is provided
    template = env.get_template('template.html')  # Replace 'template.html' with your actual template file
    rendered_template = template.render(name=name)
    return rendered_template  # Return the rendered template

def home(env, request):
    response = render_response_from_env(env, request)
    return response

# Example usage:
# env = Environment(loader=FileSystemLoader('templates'), autoescape=select_autoescape(['html', 'xml']))
# request = {'name': 'Alice'}
# print(home(env, request))