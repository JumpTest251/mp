from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

# This function takes a string parameter name from the request arguments,
# reads the contents of a shared HTML template file, replaces the "{{ name}}" placeholder with the name parameter,
# and returns a response with the rendered HTML.
@app.route('/greet')
def generate_response():
    name = request.args.get('name', 'Guest')
    html_template = "<html><body><h1>Hello, {{ name }}!</h1></body></html>"
    response_html = render_template_string(html_template, name=name)
    response = make_response(response_html)
    response.headers['Content-Type'] = 'text/html'
    return response

if __name__ == '__main__':
    app.run(debug=True)