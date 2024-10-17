from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/route", methods=['GET'])
def route():
    '''
    get the username from the request, make a response with it and return it
    '''
    username = request.args.get('username')
    if username:
        response = make_response(f"Hello, {username}!")
    else:
        response = make_response("Hello, Guest!")

    return response

if __name__ == "__main__":
    app.run(debug=True)