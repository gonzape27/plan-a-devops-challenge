#!/usr/bin/python3

from flask import Flask, jsonify
from functions import *

server = Flask(__name__)

# define default route /
@server.route("/")

# entry function to return requested json
def main():
    return jsonify({'timestamp:': return_timestamp(),
                    'hostname': return_hostname(),
                    'engine': return_engine(),
                    'visitor ip': return_visitor_ip()})

# initialization
if __name__ == "__main__":
   server.run(host='0.0.0.0', port=3000)
