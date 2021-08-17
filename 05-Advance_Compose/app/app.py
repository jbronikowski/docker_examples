import socket
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'
    
@app.route("/hostname/")
def return_hostname():
    return "This is an example wsgi app served from {}".format(socket.gethostname())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
