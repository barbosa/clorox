import sys, os, re

HEADER_TEMPLATE = r"\/\/\n\/\/.*\.swift\n\/\/.*\n\/\/\n\/\/\s{2}Created by\s.*\son\s\d{1,2}\/\d{1,2}\/\d{2}\.\n\/\/\s{2}Copyright\s\(c\)\s\d{4}\s.*\.\sAll rights reserved\.\n\/\/\n"

class Clorox:

    list_mode = False

    def __init__(self, params):
        self.list_mode = any(x in params for x in ['-l', '--list'])

    def run(self):
        total_files, modified_files = 0, 0
        for root, dirs, files_list in os.walk("."):
            for file_path in files_list:
                if not file_path.endswith(".swift"):
                    continue
                total_files = total_files + 1
                full_path = os.path.join(root, file_path)
                has_header, updated_content = self._has_xcode_header(full_path)
                if has_header:
                    if self.list_mode:
                        print full_path
                    else:
                        self._remove_header(full_path, updated_content)
                    modified_files = modified_files + 1
        print "Total files {0}".format(total_files)
        print "Modified files {0}".format(modified_files)

    def _has_xcode_header(self, file_path):
        with open(file_path, 'r') as file:
            content = file.readlines()
            header = ''.join(content[:8])
            updated_content = content[8:]
        return re.match(HEADER_TEMPLATE, header) is not None, updated_content

    def _remove_header(self, file_path, updated_content):
        with open(file_path, 'w') as file:
            file.writelines(updated_content)

if __name__ == '__main__':
    Clorox(sys.argv).run()
