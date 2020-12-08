#!/usr/bin/env python3

import sys
import re

from advent import AdventInputFileParser, AdventLineParser, LOG

#-------------------------------------------------------------------------------
# Part #1: LineParser Subclass
#-------------------------------------------------------------------------------
class PartOneLineParser(AdventLineParser):

    def parse_line(self, line):
      pass

#-------------------------------------------------------------------------------
# Part #2: LineParser Subclass
#-------------------------------------------------------------------------------
class PartTwoLineParser(AdventLineParser):

    def parse_line(self, line):
      pass

#-------------------------------------------------------------------------------
# MAIN()
#-------------------------------------------------------------------------------
def main():
  ERROR_MSG = "You must provide part# to run AND input file: <1|2> <input_file>"

  if len(sys.argv) != 3:
    print(ERROR_MSG)
    sys.exit(1)

  part_to_run = sys.argv[1]
  if part_to_run != "1" and part_to_run != "2":
    print(ERROR_MSG)
    sys.exit(1)

  input_file = sys.argv[2]
  part_class_type = PartOneLineParser if part_to_run == "1" else PartTwoLineParser

  input_parser = AdventInputFileParser(input_file, "\n", part_class_type)
  print(f"\nFINAL Count: [{input_parser.get_total()}]")


if __name__ == '__main__':
  main()

