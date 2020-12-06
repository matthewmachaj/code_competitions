#!/usr/bin/env python3

import sys
from functools import reduce

INPUT_FILE = '3.in'
#INPUT_FILE = 'test.in'

def LOG(msg, level="INFO"):
  print(msg)

#-------------------------------------------------------------------------------
# Helpers
#-------------------------------------------------------------------------------
def count_cols(line):
  count = 0
  for c in line:
    if c == "\n":
      break
    else:
      count += 1
  return count

def read_lines(input_file):
    lines = []
    with open(input_file) as input:
      lines = input.readlines()
    return lines

def count_trees_for_slope(lines, cols, right_move, down_move):
    curr_pos = 0
    num_trees = 0

    # Discard 1st line by starting range at index 1
    for i in range(down_move, len(lines), down_move):
      line = lines[i]
      curr_pos += right_move
      obj_at_curr_pos = line[curr_pos % cols]

      if obj_at_curr_pos == "#":
        num_trees += 1

    return num_trees
#-------------------------------------------------------------------------------
# MAIN()
#-------------------------------------------------------------------------------
def main():
  lines = read_lines(INPUT_FILE)
  num_cols = count_cols(lines[0])

  moves = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
  ]

  num_trees = []
  for move in moves:
    num_trees.append(count_trees_for_slope(lines, num_cols, move[0], move[1]))
    print(f"{move}: {num_trees}")

  out = num_trees[0] * num_trees[1] * num_trees[2] * num_trees[3] * num_trees[4]
  print(out)
  print(reduce(lambda x,y: x*y, num_trees))
if __name__ == '__main__':
  main()
