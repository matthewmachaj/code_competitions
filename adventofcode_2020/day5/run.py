#!/usr/bin/env python3

import sys

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
  # ERROR_MSG = "You must provide part# to run AND input file: <1|2> <input_file>"

  # if len(sys.argv) != 3:
    # print(ERROR_MSG)
    # sys.exit(1)

  # part_to_run = sys.argv[1]
  # if part_to_run != "1" and part_to_run != "2":
    # print(ERROR_MSG)
    # sys.exit(1)

  input_file = sys.argv[2]
  input = read_input(input_file)
  results = []

  for line in input:
    results.append(process_line(line))

  print(f"max(results) = {max(results)}")
  sorted = results.sort()
  last = results[0]
  for i, curr in enumerate(results):
    if i == 0:
      last = curr
      continue
    if curr != (last + 1):
      print(f"Seat # != (last + 1) => [{curr}]")
      break
    else:
      last = curr
      continue

if __name__ == '__main__':
  main()

