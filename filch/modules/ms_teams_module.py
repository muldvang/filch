import subprocess
import time

def run(callback):
    command = '''bash -c "swaymsg --type get_tree | grep 'Microsoft Teams classic' | grep -o '([0-9+])' | head -n 1 | grep -o '[0-9+]'"'''
    while True:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.stdout:
            callback(text = '󰊻', color = '#A52A2A')
        else:
            callback('')

        time.sleep(60)
