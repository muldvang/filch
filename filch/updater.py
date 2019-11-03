import sys

class Updater:
    def __init__(self, blocks):
        self.blocks = {}
        for block in blocks:
            self.updater_hook(block)('')

    def update(self, block, text, color):
        self.blocks[block] = json(block, text, color)
        self.print_json()

    def print_json(self):
        sys.stdout.write(',[' + ','.join(self.blocks.values()) + ']\n')
        sys.stdout.flush()

    def updater_hook(self, block):
        return lambda text, color=None: self.update(block, text, color)


def json(block, text, color):
    if color:
        return '{"full_text":"' + text + '","color":"' + color + '","separator":false,"separator_block_width":15}'
    else:
        return '{"full_text":"' + text + '","separator":false,"separator_block_width":15}'

