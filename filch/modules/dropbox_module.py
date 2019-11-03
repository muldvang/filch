import socket
import os
import time
from threading import Thread, Event

def run(callback):
    status = fetch_status()
    callback(render(status))

    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.connect(os.path.expanduser('~/.dropbox/iface_socket'))
    event = Event()
    updater_thread = Thread(target=lambda: update_until_up_to_date(event, callback), daemon=True)
    updater_thread.start()
    while True:
        s.recv(1024)
        status = fetch_status()
        callback(render(status))
        event.set()

def update_until_up_to_date(event, callback):
    """
    This method is used to keep refreshing the status of dropbox until it becomes 'Up to date'
    """
    while True:
        event.wait()
        event.clear()
        status = fetch_status()
        while not status == 'Up to date':
            time.sleep(1)
            status = fetch_status()
            callback(render(status))
            
def render(status):
    if status == 'Up to date':
        return ''

    return ' ' + status.replace('"', '\\"')

    
def fetch_status():
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.connect(os.path.expanduser('~/.dropbox/command_socket'))
    f = s.makefile("rw", 4096)

    def read_status(f, res):
        while True:
            line = f.readline()
            if line.startswith('status'):
                message = line.split('\t')[1].rstrip()
                res.append(message)
                return

    status = []
    recieve_thread = Thread(target=lambda: read_status(f, status))
    recieve_thread.start()

    f.write('get_dropbox_status\ndone\n')
    f.flush()
    
    recieve_thread.join()
    return status[0]
