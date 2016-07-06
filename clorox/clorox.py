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

    def run(self):
        self.printer.print_start()

        all_files, modified_files = [], []
        current_dir = None
        for root, dirs, files_list in os.walk(self.args.path):
            if root.endswith(self.IGNORED_DIRS):
                continue

            if current_dir != root:
                current_dir = root
                self.printer.print_dir(current_dir)

            for file_path in files_list:
                if not file_path.endswith(self.ALLOWED_FORMATS):
                    continue
                all_files.append(file_path)
                full_path = os.path.join(root, file_path)
                has_header, updated_content = self._has_xcode_header(full_path)
                if has_header:
                    succeeded = True
                    if not self.args.inspection:
                        succeeded = self._remove_header(full_path, updated_content)

                    modified_files.append(full_path)
                    self.printer.print_file(full_path, succeeded)

        self.printer.print_end(all_files, modified_files)

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
    parser.add_argument('-p', '--path')
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
