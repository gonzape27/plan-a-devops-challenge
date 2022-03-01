#!/usr/bin/python3

from datetime import datetime
from flask import request
import flask
import socket

#--------------------------------------------------------------------------------------------------------------------------------
# Name: return_timestamp()
#
# Desc: Generates and returns current timestamp with specific format dd-mm-yyyy HH:MM:SS
#   
# Arguments: None
# 
# Returns: Current timestamp with specific format dd-mm-yyyy HH:MM:SS
#---------------------------------------------------------------------------------------------------------------------------------

def return_timestamp():

    dt = datetime.now()
    ts = datetime.timestamp(dt)
    date_time = datetime.fromtimestamp(ts)

    # convert timestamp to string in dd-mm-yyyy HH:MM:SS
    str_date_time = date_time.strftime("%d-%m-%Y %H:%M:%S")

    return str_date_time

#--------------------------------------------------------------------------------------------------------------------------------
# Name: return_hostname()
#
# Desc: Get and returns current server hostname and the IP address
#   
# Arguments: None
# 
# Returns: Returns current hostname and the IP address
#---------------------------------------------------------------------------------------------------------------------------------

def return_hostname():
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    return hostname + " (IP: " + ip_addr + ")"

#--------------------------------------------------------------------------------------------------------------------------------
# Name: return_visitor_ip()
#
# Desc: Returns the visitor IP address by analyzing specific HTTP Headers
#   
# Arguments: None
# 
# Returns: Returns the visitor IP address
#---------------------------------------------------------------------------------------------------------------------------------

def return_visitor_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    else:
        return request.environ['HTTP_X_FORWARDED_FOR']

#--------------------------------------------------------------------------------------------------------------------------------
# Name: return_engine()
#
# Desc: Get and returns the current flask engine version
#   
# Arguments: None
# 
# Returns: Returns flask engine version
#---------------------------------------------------------------------------------------------------------------------------------

def return_engine():
    flask_version = flask.__version__
    return "Flask " + flask_version
