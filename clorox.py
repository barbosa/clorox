import os, re

# TODO
# create tests for:
# copyright symbol char
# dates with 1 or 2 digits

HEADER_TEMPLATE = r"\/\/\n\/\/.*\.swift\n\/\/.*\n\/\/\n\/\/\s{2}Created by\s.*\son\s\d{1,2}\/\d{1,2}\/\d{2}\.\n\/\/\s{2}Copyright\s\(c\)\s\d{4}\s.*\.\sAll rights reserved\.\n\/\/\n"

def has_xcode_header(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
        header = ''.join(content[:8])
        updated_content = content[8:]
    return re.match(HEADER_TEMPLATE, header) is not None, updated_content

def remove_header(file_path, updated_content):
    with open(file_path, 'w') as file:
        file.writelines(updated_content)

total_files = 0
modified_files = 0
for root, dirs, files_list in os.walk("."):
    for file_path in files_list:
        if not file_path.endswith(".swift"):
            continue
        total_files = total_files + 1
        full_path = os.path.join(root, file_path)
        has_header, updated_content = has_xcode_header(full_path)
        if has_header:
            remove_header(full_path, updated_content)
            modified_files = modified_files + 1

print "Total files {0}".format(total_files)
print "Modified files {0}".format(modified_files)
