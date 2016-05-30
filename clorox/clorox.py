# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os
import getopt
from matcher import Matcher
from printer import Printer


class Clorox:

    ALLOWED_FORMATS = ('.swift', '.h', '.m')
    IGNORED_DIRS = (
        '.xcdatamodel', '.xcdatamodeld'
        '.xcassets', '.imageset',
        '.bundle', '.framework', '.lproj'
    )

    def __init__(self, root_path, passive):
        self.root_path = root_path
        self.passive = passive
        self.printer = Printer(root_path, passive)

    def run(self):
        total_files, modified_files = 0, 0
        current_dir = None
        for root, dirs, files_list in os.walk(self.root_path):
            if root.endswith(self.IGNORED_DIRS):
                continue

            if current_dir != root:
                current_dir = root
                self.printer.print_dir(current_dir)

            for file_path in files_list:
                if not file_path.endswith(self.ALLOWED_FORMATS):
                    continue
                total_files = total_files + 1
                full_path = os.path.join(root, file_path)
                has_header, updated_content = self._has_xcode_header(full_path)
                if has_header:
                    succeeded = True
                    if not self.passive:
                        succeeded = self._remove_header(full_path, updated_content)

                    modified_files = modified_files + 1
                    self.printer.print_file(full_path, succeeded)

        print "\nTotal files: {0}".format(total_files)
        if self.passive:
            print "Files it would modify: {0}".format(modified_files)
        else:
            print "Modified files: {0}".format(modified_files)

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
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "hp", ["help", "passive"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    if not args:
        usage()
        sys.exit(2)

    passive = False
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        if opt in ("-p", "--passive"):
            passive = True

    root_path = "".join(args)
    Clorox(root_path, passive).run()


def usage():
    print "Usage:"
    print "    clorox [OPTIONS] [PATH]"
    print
    print "Parameters:"
    print "    path                Path to run clorox"
    print
    print "Options:"
    print "    --passive, -p       prints the output without running the script"
    print "    --help, -h          prints this help message"


if __name__ == '__main__':
    main()
