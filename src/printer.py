# !/usr/bin/python
# -*- coding: utf-8 -*-
import os

class Printer:

    def __init__(self, root_path, passive):
        self.root_path = root_path
        self.passive = passive

    def print_start(self):
        print u'{0} Running '

    def print_dir(self, path):
        dir_name = os.path.basename(path)
        print Color.PURPLE + u'{0}{1}/'.format('  ' * self._get_depth(path), dir_name) + Color.END

    def print_file(self, path, succeeded=True):
        file_name = os.path.basename(path)
        color = Color.RED if not succeeded else Color.END
        label_color = Color.YELLOW if self.passive else Color.GREEN
        feedback = '(would be modified)' if self.passive else '(done)'
        print u'{0}{1} {2}'.format('  ' * self._get_depth(path), self._colored(file_name, color), self._colored(feedback, label_color))

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
