import subprocess
import pulsectl


def run(callback):
    callback(text())

    with pulsectl.Pulse('event-printer') as pulse:
        def update(ev):
            if (ev.t == pulsectl.PulseEventTypeEnum.change):
                callback(text())

        pulse.event_mask_set('all')
        pulse.event_callback_set(update)
        pulse.event_listen()


def text():
    return '墳 ' + sink() + ': ' + volume() + ' %'


def sink():
    bash_script = '''
    PAC=$(pacmd list-sinks | grep -P "\*" --after-context 36)
    SINK=$(pacmd list-sinks | grep -P "\*" --after-context 1000| grep 'device.description' | head -n1 | cut -d '"' -f 2 | sed 's/ Audio Analog Stereo//g' | sed 's/ Series Analog Stereo//g')
    echo -n "$SINK"
    '''
    process = subprocess.run(['bash', '-c', bash_script], stdout=subprocess.PIPE)
    return process.stdout.decode('utf-8')


def volume():
    bash_script = '''
    PAC=$(pacmd list-sinks | grep -P "\*" --after-context 36)
    VOLUME=$(echo "$PAC" | grep -P [0-9]+% -o | head -n 1 | tr -d '%')
    echo -n "$VOLUME"
    '''
    process = subprocess.run(['bash', '-c', bash_script], stdout=subprocess.PIPE)
    return process.stdout.decode('utf-8')
