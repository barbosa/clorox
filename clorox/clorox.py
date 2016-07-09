# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os
import argparse
from matcher import Matcher
from printer import Printer


class Clorox:

    ALLOWED_FORMATS = ('.swift', '.h', '.m')
    IGNORED_DIRS = (
        '.xcdatamodel', '.xcdatamodeld'
        '.xcassets', '.imageset',
        '.bundle', '.framework', '.lproj'
    )

    def __init__(self, args):
        self.args = args
        self.printer = Printer(args)
        self.all_files, self.modified_files = [], []

    def run(self):
        self.printer.print_start()

        current_dir = None
        for path in self.args.path:
            if os.path.isfile(path):
                self._process_file(path)
            elif os.path.isdir(path):
                for dirpath, dirnames, filenames in os.walk(path):
                    if dirpath.endswith(self.IGNORED_DIRS):
                        continue

                    if current_dir != dirpath:
                        current_dir = dirpath
                        self.printer.print_dir(current_dir)

                    for filename in filenames:
                        if filename.endswith(self.ALLOWED_FORMATS):
                            self._process_file(os.path.join(dirpath, filename))

        self.printer.print_end(self.all_files, self.modified_files)

    def _process_file(self, file_path):
        self.all_files.append(file_path)
        has_header, updated_content = self._has_xcode_header(file_path)
        if has_header:
            succeeded = True
            if not self.args.inspection:
                succeeded = self._remove_header(file_path, updated_content)

            self.modified_files.append(file_path)
            self.printer.print_file(file_path, succeeded)

    def _has_xcode_header(self, file_path):
        with open(file_path, 'r') as file:
            content = file.readlines()
            header_height = Matcher.HEADER_TEMPLATE.count('\n')
            for line in range(header_height, len(content)):
                if content[line] == '\n':
                    header_height = header_height + 1
                else:
                    break

            header = ''.join(content[:header_height])
            updated_content = content[header_height:]
        return Matcher(header).matches(), updated_content

    def _remove_header(self, file_path, updated_content):
        try:
            with open(file_path, 'w') as file:
                file.writelines(updated_content)
                return True
        except Exception:
            return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', nargs='+', required=True)
    parser.add_argument('-i', '--inspection', dest='inspection', action='store_true')
    parser.add_argument('-q', '--quiet', dest='quiet', action='store_true')
    parser.add_argument('-r', '--reporter', choices=['json'])
    args = parser.parse_args()

    if not args.path:
        print 'You must provide a directory to be cleaned using the --dir option'
        sys.exit(2)

    Clorox(args).run()

if __name__ == '__main__':
    main()
