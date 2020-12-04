#!/usr/bin/env python3

import sys
import re

INPUT_FILE = '3.in'

def LOG(msg, level="INFO"):
  print(msg)

#-------------------------------------------------------------------------------
# MAIN()
#-------------------------------------------------------------------------------
def count_cols(line):
  count = 0
  for c in line:
    if c == "\n":
      break
    else:
      count += 1
  return count

def main():
  MOVES_RIGHT = 3

  num_cols = None
  with open(INPUT_FILE) as input:
    # Use 1st line to count cols then discard
    first_line = input.readline()
    num_cols = count_cols(first_line)

    curr_pos = 0
    num_trees = 0
    for line in input:
      curr_pos += MOVES_RIGHT
      obj_at_curr_pos = line[curr_pos % num_cols]
      if obj_at_curr_pos == "#":
        num_trees += 1

    print(num_trees)

if __name__ == '__main__':
  main()
