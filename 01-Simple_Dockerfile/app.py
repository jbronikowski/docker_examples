import socket
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flasks in a Docker container!'
    
@app.route("/hostname/")
def return_hostname():
    return "This is an example wsgi app served from {} to {}".format(socket.gethostname(), request.remote_addr)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
