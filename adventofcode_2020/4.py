#!/usr/bin/env python3

import sys

INPUT_FILE = '4.in.test'
INPUT_FILE = '4.in'

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

  def is_valid(self):
    num_keys = len(self.fields.keys())
    if num_keys == 8:
      return True
    elif num_keys == 7 and not ('cid' in self.fields):
      return True
    else:
      return False

  def __str__(self):
    return f"[PASSPORT]\n{self.data}"

#-------------------------------------------------------------------------------
# MAIN()
#-------------------------------------------------------------------------------
def main():
  passports = read_passports(INPUT_FILE)
  valid_count = 0
  for p in passports:
    if p.is_valid():
      valid_count += 1
  print(valid_count)

if __name__ == '__main__':
  main()
