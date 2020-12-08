#!/usr/bin/env python3

import sys
import re

from advent import LOG
from advent import AdventInputFileParser
from advent import AdventLineParser
from advent import AdventParsedLineSummarizer

#-------------------------------------------------------------------------------
# Part #1: LineParser Subclass
#-------------------------------------------------------------------------------
class PartOneLineParser(AdventLineParser):

  def parse_line(self, line):
    line = line.replace("\n","")
    letter_set = set()
    for letter in line:
      letter_set.add(letter)
    print(letter_set)
    return len(letter_set)

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

  INPUT_FILE = sys.argv[2]
  PART_PARSER = PartOneLineParser() if part_to_run == "1" else PartTwoLineParser()

  #input_parser = AdventInputFileParser(PART_PARSER, AdventInputFileParser.ONE_LINE_PER_OBJ)
  input_parser = AdventInputFileParser(PART_PARSER, AdventInputFileParser.MULTI_LINE_PER_OBJ)
  parsed_objs = input_parser.parse_file(INPUT_FILE)

  summarizer = AdventParsedLineSummarizer()
  final_count = summarizer.get_total(parsed_objs)
  print(f"\nFINAL Count: [{final_count}]")


if __name__ == '__main__':
  main()

