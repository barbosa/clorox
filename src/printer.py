# !/usr/bin/python
# -*- coding: utf-8 -*-
import os

class Printer:

    def __init__(self, root_path):
        self.root_path = root_path

    def print_path(self, path):
        name = os.path.basename(path)
        if os.path.isdir(path):
            print Color.HEADER + u'{0}{1}/'.format('  ' * self._get_depth(path), name) + Color.END
        else:
            print u'{0}{1}'.format('  ' * self._get_depth(path), name)

    def _get_depth(self, path):
        if path == self.root_path:
            return 0
        if os.path.isdir(path):
            return len(os.path.relpath(path, self.root_path).split('/'))
        else:
            return self._get_depth(os.path.dirname(path)) + 1

class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Emoji:
    CHECKMARK = u'\U00002705'
