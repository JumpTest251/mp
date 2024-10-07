import re
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/redirect')
def redirect_target():
    target = request.args.get('target', '')
    regex = r'^[\w-]+\.'  # Matches one or more alphanumeric characters or hyphens followed by a period

    if re.match(regex, target):
        return redirect(target)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)