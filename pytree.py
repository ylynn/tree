#!/usr/bin/env python3

import sys
import os



def print_tree(path, count, indent=''):
    items = os.listdir(path)
    items = [item for item in items if item[0] != '.']
    for i, files in enumerate(items):
        fullpath = path + "/" + files
        count[1] = count[1] + 1
        sign = 0
        if i == len(items) - 1: 
            sign = 1 
        if sign == 1:
            print(indent + '└── ' + files)
        else:
            print(indent + '├── ' + files)
        if os.path.isdir(fullpath):
            count[0] = count[0] + 1
            if sign == 1:
                print_tree(fullpath, count, indent + '   ')
            else:
                print_tree(fullpath, count, indent + '│   ')


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
