# !/usr/bin/python
# -*- coding: utf-8 -*-
import os
from reporter import Reporter

class Printer:

    def __init__(self, args):
        self.args = args
        reporting = hasattr(args, 'reporter')
        self.reporter = Reporter.from_identifier(args.reporter) if reporting else None

    def print_start(self):
        self._print(u'Running...')

    def print_dir(self, path):
        dirname = os.path.basename(path)
        tabs = self._tabs(path)
        self._print(Color.PURPLE + u'{0}{1}/'.format(tabs, dirname) + Color.END)

    def print_file(self, path, succeeded=True):
        file_name = os.path.basename(path)
        color = Color.RED if not succeeded else Color.END
        label_color = Color.YELLOW if self.args.inspection else Color.GREEN
        feedback = '(would be modified)' if self.args.inspection else '(done)'

        self._print(
            u'{0}{1} {2}'.format(self._tabs(path),
                self._colored(file_name, color),
                self._colored(feedback, label_color)
            )
        )

    def _tabs(self, path):
        return ' ' * 2 * len(path.split('/'))

    def print_end(self, all_files, modified_files):
        if self.reporter:
            self.reporter.report(all_files, modified_files)
        else:
            self._print("\nTotal files: {0}".format(len(all_files)))
            if self.args.inspection:
                self._print("Files it would modify: {0}".format(len(modified_files)))
            else:
                self._print("Modified files: {0}".format(len(modified_files)))

    def _print(self, message):
        if not self.args.quiet and self.reporter is None:
            print message

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
