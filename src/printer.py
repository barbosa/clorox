# !/usr/bin/python
# -*- coding: utf-8 -*-
import os

class Printer:

    def __init__(self, root_path, passive):
        self.root_path = root_path
        self.passive = passive

    def print_start(self):
        print u'{0} Running '

    def print_path(self, path):
        name = os.path.basename(path)
        if os.path.isdir(path):
            print Color.PURPLE + u'{0}{1}/'.format('  ' * self._get_depth(path), name) + Color.END
        else:
            color = Color.YELLOW if self.passive else Color.GREEN
            feedback = '(would be modified)' if self.passive else '(done)'
            print u'{0}{1} {2}'.format('  ' * self._get_depth(path), name, self._colored(feedback, color))

    def _get_depth(self, path):
        if path == self.root_path:
            return 0
        if os.path.isdir(path):
            return len(os.path.relpath(path, self.root_path).split('/'))
        else:
            return self._get_depth(os.path.dirname(path)) + 1

    def _colored(self, string, color):
        return '%s%s%s' % (color, string, Color.END)

class Color:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Emoji:
    CHECKMARK = u'\U00002705'
    ROCKET = u'\U0001F680'
