#!/usr/bin/env python3

import sys

INPUT_FILE = '5.in.test'
INPUT_FILE = '5.in'

def LOG(msg, level="INFO"):
  print(msg)

#-------------------------------------------------------------------------------
# Helpers
#-------------------------------------------------------------------------------
def read_input(input_file):
    with open(input_file) as input:
      return input.readlines()

def process_line(line):
  row_letters = line[0:7]
  col_letters = line[7:10]

  row = ["1" if l == "B" else "0" for l in row_letters ]
  col = ["1" if l == "R" else "0" for l in col_letters ]

  row = int("".join(row), 2)
  col = int("".join(col), 2)

  return (row * 8) + col


#-------------------------------------------------------------------------------
# MAIN()
#-------------------------------------------------------------------------------
def main():
  input = read_input(INPUT_FILE)
  results = []

  for line in input:
    results.append(process_line(line))

  print(max(results))

if __name__ == '__main__':
  main()
