#!/usr/bin/env python3

import sys
import re

INPUT_FILE = '4.in.test'
INPUT_FILE = '4.in'
#INPUT_FILE = '4.part2.test.in'

LOG_LEVEL = "INFO"

def LOG(msg, level="INFO"):
  level = LOG_LEVEL

  if level == "DEBUG":
    print(f"DBG: {msg}")

#-------------------------------------------------------------------------------
# Helpers
#-------------------------------------------------------------------------------

def read_passports(input_file):
    passports = []
    with open(input_file) as input:
      passport_data = ""
      for line in input:
        if line != "\n":
          LOG(line)
          passport_data += line
        else:
          p = Passport(passport_data)
          passports.append(p)
          passport_data = ""
      passports.append(Passport(passport_data))
    return passports

class Passport:

  def __init__(self, data):
    self.data = data
    self.fields = self.parse_data()

  def parse_data(self):
    field_list = self.data.replace("\n", " ").strip().split(" ")
    field_list = [f.split(":") for f in field_list]
    return dict(field_list)

    LOG(f"Fields Dict: {self.fields}")

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


  #  print(f"Returning -> {ret_val} : {bad_field}")
    return ret_val

  def __str__(self):
    return f"[PASSPORT]\n{self.data}"

#-------------------------------------------------------------------------------
# MAIN()
#-------------------------------------------------------------------------------
def main():
  passports = read_passports(INPUT_FILE)
  valid_count = 0
  for p in passports:
  #  print(p)
    if p.is_valid():
      valid_count += 1
  print(valid_count)

if __name__ == '__main__':
  main()
