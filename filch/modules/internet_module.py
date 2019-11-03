import subprocess
import time
import socket

def run(callback):
    connection_established = connected()
    callback(text = text(connection_established), color = color(connection_established))

    while True:
        connection_established = connected()
        callback(text = text(connection_established), color = color(connection_established))
        time.sleep(5)

def text(con):
    if con:
        return ''
    else:
        return ' No internet connection'

def color(con):
    if con:
        return '#4E9A06'
    else:
        return '#A52A2A'


def connected():
    try:
        socket.gethostbyaddr('8.8.8.8')
        return True
    except:
        return False

