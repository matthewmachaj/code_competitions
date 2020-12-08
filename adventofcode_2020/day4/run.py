#!/usr/bin/env python3

import sys
import re

from advent import AdventInputFileParser
from advent import AdventLineParser
from advent import AdventParsedLineSummarizer
from advent import LOG


class Passport:

  def __init__(self, data):
    self.data = data
    self.fields = self.parse_data()

  def parse_data(self):
    field_list = self.data.replace("\n", " ").strip().split(" ")
    field_list = [f.split(":") for f in field_list]
    return dict(field_list)

  # byr (Birth Year) - four digits; at least 1920 and at most 2002.
  # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
  # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
  # hgt (Height) - a number followed by either cm or in:
  # If cm, the number must be at least 150 and at most 193.
  # If in, the number must be at least 59 and at most 76.
  # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
  # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
  # pid (Passport ID) - a nine-digit number, including leading zeroes.
  # cid (Country ID) - ignored, missing or not.
  def is_valid(self):
    num_keys = len(self.fields.keys())
    keys = self.fields.keys()

    bad_field = ""
    ret_val = True

    if "byr" in keys:
      byr = int(self.fields["byr"])
      if not (byr >= 1920 and byr <= 2002):
        bad_field += ",byr"
        ret_val = False
    else:
      bad_field += ",byr"
      ret_val = False

    if "iyr" in keys:
      f = int(self.fields["iyr"])
      if not (f >= 2010 and f <= 2020):
        bad_field += ",iyr"
        ret_val = False
    else:
      bad_field += ",iyr"
      ret_val = False

    if "eyr" in keys:
      f = int(self.fields["eyr"])
      if not (f >= 2020 and f <= 2030):
        bad_field += ",eyr"
        ret_val = False
    else:
      bad_field += ",eyr"
      ret_val = False

    if "hgt" in keys:
      f = self.fields["hgt"]
      matcher = re.compile(r'([0-9]+)([a-z]+)').match(f)
      if matcher == None:
        bad_field += ",hgt"
        ret_val = False
      else:
        val = int(matcher.group(1))
        unit = matcher.group(2)

        if unit == "cm":
          if not (val >= 150 and val <= 193):
            bad_field += ",hgt"
            ret_val = False
        else:
          if not (val >= 59 and val <= 76):
            bad_field += ",hgt"
            ret_val = False
    else:
      bad_field += ",hgt"
      ret_val = False

    if "hcl" in keys:
      f = self.fields["hcl"]
      matcher = re.compile(r'#([0-9a-z]{6})').match(f)
      if matcher == None:
        bad_field += ",hcl"
        ret_val = False
    else:
      bad_field += ",hcl"
      ret_val = False

    if "ecl" in keys:
      f = self.fields["ecl"]
      matcher = re.compile(r'(amb|blu|brn|gry|grn|hzl|oth)').match(f)
      if matcher == None:
        bad_field += ",ecl"
        ret_val = False
    else:
      bad_field += ",ecl"
      ret_val = False

    if "pid" in keys:
      f = self.fields["pid"]
      matcher = re.compile(r'^[0-9]{9}$').match(f)
      if matcher == None:
        bad_field += ",pid"
        ret_val = False
    else:
      bad_field += ",pid"
      ret_val = False

    LOG(f"Returning -> {ret_val} : {bad_field}")
    return ret_val

  def __str__(self):
    return f"[PASSPORT]\n{self.data}"

#-------------------------------------------------------------------------------
# Part #1: LineParser Subclass
#-------------------------------------------------------------------------------
class PartOneLineParser(AdventLineParser):
  def parse_line(self, line):
    passport = Passport(line)
    is_valid = passport.is_valid()
    return 1 if is_valid else 0

#-------------------------------------------------------------------------------
# Part #2: LineParser Subclass
#-------------------------------------------------------------------------------
class PartTwoLineParser(AdventLineParser):

  def parse_line(self, line):
    passport = Passport(line)
    is_valid = passport.is_valid()
    return 1 if is_valid else 0

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
  part_parser = PartOneLineParser() if part_to_run == "1" else PartTwoLineParser()

  input_parser = AdventInputFileParser(part_parser, AdventInputFileParser.MULTI_LINE_PER_OBJ)
  parsed_objs = input_parser.parse_file(input_file)

  summarizer = AdventParsedLineSummarizer()
  final_count = summarizer.get_total(parsed_objs)
  print(f"\nFINAL Count: [{final_count}]")


if __name__ == '__main__':
  main()

