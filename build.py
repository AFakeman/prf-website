import glob
import os
import re
import sys
import warnings


file_cache = {}


def include_file(match):
    global root
    if not match:
        return
    file = match.group(2)
    file = file.lstrip('/')
    file = os.path.join(root, file)

    if os.path.exists(file):
        process_file(file)
    else:
        file_cache[file] = ""
        warnings.warn("{} does not exist".format(file), RuntimeWarning)

    return file_cache[file]


def process_file(file):
    if file in file_cache:
        return

    with open(file) as f:
        contents = f.read()

    contents = re.sub(r'<!--\s*#include\s*(virtual|file)=[\'"]([^\'"]+)[\'"]\s*-->', include_file, contents)

    file_cache[file] = contents

    with open(file, 'w') as f:
        f.write(contents)


if __name__ == "__main__":
    global root
    root = sys.argv[1]
    root = os.path.abspath(root)
    for file in glob.iglob(root + "/**/*.html", recursive=True):
        process_file(file)
