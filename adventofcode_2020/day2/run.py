#!/usr/bin/env python3

import sys
import re

from advent import AdventInputFileParser, AdventLineParser, LOG

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

        return pass_ok

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

