#!/usr/bin/env python3

import sys
import re

INPUT_FILE = '2.in'

def DBG(msg, level="INFO"):
    print(msg)

#-------------------------------------------------------------------------------
# MAIN()
#-------------------------------------------------------------------------------
def read_lines(input_file):
    lines = []
    with open(input_file) as input:
        lines = input.readlines()
    return lines

def main():
    lines = read_lines(INPUT_FILE)

    line_parser = PartOneLineParser()
    line_parser = PartTwoLineParser()
    parsed_lines = line_parser.parse_lines(lines)

    print(parsed_lines.count(True))

#-------------------------------------------------------------------------------
# Line Parser Parent Class
#-------------------------------------------------------------------------------
class LineParser:

    # def __init__(self):
        # pass

    def parse_lines(self, lines):
        parsed_lines = []
        for i, line in enumerate(lines):
            parsed_lines.append(self.parse_line(line))
        return parsed_lines

#-------------------------------------------------------------------------------
# PartOne Line Parser Subclass
#-------------------------------------------------------------------------------
class PartOneLineParser(LineParser):

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

        DBG(f"Line: {line}COUNT={count}, OK={pass_ok}, lower={lower}, upper={upper},letter={letter}, pass={password}")

        return pass_ok

#-------------------------------------------------------------------------------
# PartTwo Line Parser Subclass
#-------------------------------------------------------------------------------
class PartTwoLineParser(LineParser):

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

        DBG(f"Line: {line}OK={pass_ok}, first={firstPosition}, last={lastPosition},letter={letter}, pass={password}")

        return pass_ok

if __name__ == '__main__':
  main()
