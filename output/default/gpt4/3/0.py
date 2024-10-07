from flask import Flask, redirect, request
import re

app = Flask(__name__)

# Regular expression to match URLs containing 'example.com'
url_pattern = re.compile(r'https?://(?:www\.)?example\.com')

@app.route('/redirect')
def redirect_to_target():
    target = request.args.get('target')
    
    if target and url_pattern.match(target):
        return redirect(target)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)