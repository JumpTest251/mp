import re
from flask import Flask, redirect

app = Flask(__name__)

# Compiled regular expression for matching the target URL
TARGET_URL_REGEX = re.compile(r'^https?://(www\.)?example\.com/.*$')
DEFAULT_REDIRECT_URL = 'https://www.default.com'

@app.route('/redirect/<path:url>')
def redirect_to_url(url):
    target_url = f"https://{url}"
    if TARGET_URL_REGEX.match(target_url):
        return redirect(target_url, code=302)
    else:
        return redirect(DEFAULT_REDIRECT_URL, code=302)

if __name__ == '__main__':
    app.run(debug=True)