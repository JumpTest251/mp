import re
from flask import Flask, redirect, request

app = Flask(__name__)

# Compile the regular expression once at module load
url_pattern = re.compile(r'^https?://(www\.)?example\.com/.*$')  # Adjust the pattern as needed
default_url = 'https://default-url.com'

@app.route('/redirect', methods=['GET'])
def redirect_to_url():
    target_url = request.args.get('url')

    if target_url and url_pattern.match(target_url):
        return redirect(target_url, code=302)
    else:
        return redirect(default_url, code=302)

if __name__ == '__main__':
    app.run(debug=True)