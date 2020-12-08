#!/usr/bin/env python3

import sys
import re

from advent import LOG
from advent import AdventInputFileParser
from advent import AdventLineParser
from advent import AdventParsedLineSummarizer

#-------------------------------------------------------------------------------
# PartOne Line Parser Subclass
#-------------------------------------------------------------------------------
class PartOneLineParser(AdventLineParser):

    # Example line:
    #4-6 b: bbbdbtbbbj
    def parse_line(self, line):
        matcher = re.compile(r'^(\d+)-(\d+) ([a-z]{1}): ([a-z]+)$')
        matched = matcher.match(line)

        lower = int(matched.group(1))
        upper = int(matched.group(2))
        letter = matched.group(3)
        password = matched.group(4)

        count = password.count(letter)
        if count >= lower and count <= upper:
            pass_ok = True
        else:
            pass_ok = False

        LOG(f"Line: {line}COUNT={count}, OK={pass_ok}, lower={lower}, upper={upper},letter={letter}, pass={password}")

        return 1 if pass_ok else 0

#-------------------------------------------------------------------------------
# PartTwo Line Parser Subclass
#-------------------------------------------------------------------------------
class PartTwoLineParser(AdventLineParser):

    # Example line:
    #4-6 b: bbbdbtbbbj
    def parse_line(self, line):
        matcher = re.compile(r'^(\d+)-(\d+) ([a-z]{1}): ([a-z]+)$')
        matched = matcher.match(line)

        firstPosition = int(matched.group(1))
        lastPosition = int(matched.group(2))
        letter = matched.group(3)
        password = matched.group(4)

        charAtFirst = password[firstPosition-1]
        charAtLast = password[lastPosition-1]
        if (charAtFirst == letter and (charAtLast != letter)) or ((charAtFirst != letter) and charAtLast == letter):
            pass_ok = True
        else:
            pass_ok = False

        LOG(f"Line: {line}OK={pass_ok}, first={firstPosition}, last={lastPosition},letter={letter}, pass={password}")

        return 1 if pass_ok else 0

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

  input_parser = AdventInputFileParser(PART_PARSER, AdventInputFileParser.ONE_LINE_PER_OBJ)
  parsed_objs = input_parser.parse_file(INPUT_FILE)

  summarizer = AdventParsedLineSummarizer()
  final_count = summarizer.get_total(parsed_objs)
  print(f"\nFINAL Count: [{final_count}]")


if __name__ == '__main__':
  main()

