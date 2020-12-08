#!/usr/bin/env python3

def LOG(msg):
  print(msg)

#-------------------------------------------------------------------------------
# Input File Parser:
#
# Parses over entire input file to convert the lines of input into "advent
# objects", where X number of input lines correspond to an object depending
# on the specifics of the daily challenge.
#-------------------------------------------------------------------------------
class AdventInputFileParser:

  def __init__(self, input_file, delimiter, line_parser_type):
    self.input_file = input_file
    self.delimiter = delimiter
    self.line_parser_type = line_parser_type
    self.parsed_objects = self.parse_input(self.input_file)

  def parse_input(self, input_file):
    parsed_objects = []

    with open(input_file) as input:
      if self.delimiter == "\n":
        for line in input:
          parsed_objects.append(self.line_parser_type(line))

    return parsed_objects

  def get_total(self):
    total = 0
    for obj in self.parsed_objects:
      total += obj.get_val()

    return total

#-------------------------------------------------------------------------------
# Input Line Parser:
#
# A superclass whose parse_line() method is meant to parse one or more lines
# from a daily input file that represent a single object, and then translate
# that into some sort of value that is being counted for that daily challenge.
#-------------------------------------------------------------------------------
class AdventLineParser:
  def __init__(self, line):
    self.line = line
    self.val = self.parse_line(self.line)

  def get_val(self):
    return self.val

  # @ToOverride
  def parse_line(self, line):
    LOG(f"IN AdventLineParser.parse_line() -> should have been OVERRIDDEN")

