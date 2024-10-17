from flask import Flask, redirect, abort, request

app = Flask(__name__)

@app.route('/redirect/<path:url>', methods=['GET'])
def redirect_invalid_url(url):
    if url.startswith('example.com'):
        return redirect(f'http://{url}', code=302)
    else:
        return abort(400, description='Invalid URL: Only example.com is allowed.')

if __name__ == '__main__':
    app.run(debug=True)