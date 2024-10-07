from jinja2 import Environment

def render_response_from_env(env, request):
    name = request.get('name')
    template = env.get_template('template.html')
    rendered_template = template.render(name=name)
    return rendered_template

def home(env, request):
    response = render_response_from_env(env, request)
    return response