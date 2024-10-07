from urllib.parse import urlparse
from flask import Flask, redirect, abort

app = Flask(__name__)

@app.route('/redirect_url/<path:url>')
def redirect_url(url):
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc

    if domain_name == 'example.com':
        return redirect(url)
    else:
        return abort(404)

if __name__ == '__main__':
    app.run()