#!/usr/bin/env python3

import sys
import os
import re


def sort_key(s):
    return re.sub('[^A-Za-z]+', '', s).lower()

def print_tree(path, count, indent=''):
    items = os.listdir(path)
    items = [item for item in items if item[0] != '.']
    items = sorted(items, key = sort_key)
    
    for i, files in enumerate(items):
        fullpath = path + "/" + files
        count[1] = count[1] + 1
        if i == len(items) - 1:
            print(indent + '└── ' + files)
            sub_indent = '   '
        else:
            print(indent + '├── ' + files)
            sub_indent = '│   '
        if os.path.isdir(fullpath):
            count[0] = count[0] + 1
            print_tree(fullpath, count, indent + sub_indent)

            
if __name__ == '__main__':
    if (len(sys.argv) == 1):
        dirname = "."
        count = [0, 0]
    elif (len(sys.argv) == 2):
        dirname = sys.argv[1]
        count = [0, 0]
    else:
        print('Wrong Input')
        sys.exit()
    print(dirname)
    print_tree(dirname, count)
    print()
    print('%d directories, %d files' % (count[0], count[1] - count[0]))
