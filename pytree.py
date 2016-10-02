#!/usr/bin/env python3

import sys
import os

def print_tree(path, count, indent=''):
  items = os.listdir(path)
  for i, files in enumerate(items):
    fullpath = path + "/" + files
    if i == len(items) - 1:
      print(indent + '`-- ' + files)
      count[1] = count[1] + 1
      if os.path.isdir(fullpath):
        print_tree(fullpath, count, indent+'   ')
        count[0] = count[0] + 1
    else:
      print(indent + '|-- ' + files)
      count[1] = count[1] + 1
      if os.path.isdir(fullpath):
        print_tree(fullpath, count, indent+'|   ')
        count[0] = count[0] + 1

if __name__ == '__main__' :
  if (len(sys.argv) == 1):
    dirname = "."
    count = [0, 0]
  elif (len(sys.argv) == 2):
    dirname= sys.argv[1]
    count = [0, 0]
  else:
    print('Wrong Input')
    sys.exit()
  print(dirname)
  print_tree(dirname, count)
  print()
  print('%d directories, %d files' % (count[0], count[1]-count[0]))
