# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os
import getopt
from matcher import Matcher


class Clorox:

    ALLOWED_FORMATS = ('.swift', '.h', '.m')

    def __init__(self, root_path, passive):
        self.root_path = root_path
        self.passive = passive

    def run(self):
        total_files, modified_files = 0, 0
        current_dir = None
        for root, dirs, files_list in os.walk(self.root_path):
            for file_path in files_list:
                if not file_path.endswith(self.ALLOWED_FORMATS):
                    continue
                total_files = total_files + 1
                full_path = os.path.join(root, file_path)
                has_header, updated_content = self._has_xcode_header(full_path)
                if has_header:
                    if not self.passive:
                        self._remove_header(full_path, updated_content)

                    modified_files = modified_files + 1

                    if current_dir != root:
                        current_dir = root
                        self._print_tabbed(current_dir)
                    self._print_tabbed(full_path)

        print "Total files {0}".format(total_files)
        if self.passive:
            print "Not yet modified files: {0}".format(modified_files)
        else:
            print "Modified files: {0}".format(modified_files)

    def _get_depth(self, path):
        if path == self.root_path:
            return 0
        if os.path.isdir(path):
            return len(os.path.relpath(path, self.root_path).split('/'))
        else:
            return self._get_depth(os.path.dirname(path)) + 1

    def _print_tabbed(self, path):
        name = os.path.basename(path)
        if os.path.isdir(path):
            print '{0}[{1}]'.format('  ' * self._get_depth(path), name)
        else:
            print '{0}{1}'.format('  ' * self._get_depth(path), name)

    def _has_xcode_header(self, file_path):
        with open(file_path, 'r') as file:
            content = file.readlines()
            header_height = Matcher.HEADER_TEMPLATE.count('\n') + 1
            header = ''.join(content[:header_height])
            updated_content = content[header_height:]
        return Matcher(header).matches(), updated_content

    def _remove_header(self, file_path, updated_content):
        with open(file_path, 'w') as file:
            file.writelines(updated_content)


def main(argv):
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
    print "    clorox [PATH] [OPTIONS]"
    print
    print "Parameters:"
    print "    path                Path to run clorox"
    print
    print "Options:"
    print "    --passive, -p       prints the output without running the script"
    print "    --help, -h          prints this help message"


if __name__ == '__main__':
    main(sys.argv[1:])
