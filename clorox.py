import sys, os, re
import getopt


class Matcher:

    HEADER_TEMPLATE = r"\/\/\n\/\/.*\..*\n\/\/.*\n\/\/\n\/\/\s{2}Created by\s.*\son\s\d{1,2}\/\d{1,2}\/\d{2}\.\n\/\/\s{2}Copyright\s\(c\)\s\d{4}\s.*\.\sAll rights reserved\.\n\/\/\n"

    def __init__(self, header):
        self.header = header

    def matches(self):
        return re.match(self.HEADER_TEMPLATE, self.header) is not None

class Clorox:

    ALLOWED_FORMATS = ('.swift', '.h', '.m')

    def __init__(self, passive):
        self.passive = passive

    def run(self):
        total_files, modified_files = 0, 0
        for root, dirs, files_list in os.walk('.'):
            for file_path in files_list:
                if not file_path.endswith(self.ALLOWED_FORMATS):
                    continue
                total_files = total_files + 1
                full_path = os.path.join(root, file_path)
                has_header, updated_content = self._has_xcode_header(full_path)
                if has_header:
                    if self.passive:
                        print full_path
                    else:
                        self._remove_header(full_path, updated_content)
                    modified_files = modified_files + 1

        print "Total files {0}".format(total_files)
        if self.passive:
            print "Not yet modified files: {0}".format(modified_files)
        else:
            print "Modified files: {0}".format(modified_files)

    def _has_xcode_header(self, file_path):
        with open(file_path, 'r') as file:
            content = file.readlines()
            header = ''.join(content[:8])
            updated_content = content[8:]
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

    passive = False
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        if opt in ("-p", "--passive"):
            passive = True

    Clorox(passive).run()

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
