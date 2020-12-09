#!/usr/bin/env python3

import sys
import re

from advent import LOG
from advent import AdventInputFileParser
from advent import AdventLineParser
from advent import AdventLogger
from advent import AdventParsedLineSummarizer

LOG_LEVEL = "DEBUG"
logger = AdventLogger(LOG_LEVEL)

#-------------------------------------------------------------------------------
# Part #1: LineParser Subclass
#-------------------------------------------------------------------------------
class Accumulator():

  ACC = 100
  JMP = 200
  NOP = 300

  def __init__(self, input_file):
    self.input_file = input_file

  def load_commands(self):
    cmds = []
    with open(self.input_file) as input:
      cmds = input.readlines()
    return cmds

  def run(self):
    INSTRUCTION_PTR = 0
    ACCUMULATOR = 0
    cmds = self.load_commands()

    while True:
      curr_cmd = cmds[INSTRUCTION_PTR]
      logger.log(f"INSTRUCTION_PTR -> {INSTRUCTION_PTR}", "INFO")

      # None value indicates command already has been executed so return accumulator value
      if curr_cmd == None:
        return ACCUMULATOR

      (op, arg) = self.parse_cmd(curr_cmd)
      print(f"PARSED: [{op}, {arg}]")
      logger.log(f"INSTRUCTION_PTR = {INSTRUCTION_PTR}")
      logger.log(f"ACCUMULATOR = {ACCUMULATOR}")
      logger.log("\n")

      # Mark command as having been done (before we increment instruction ptr below)
      cmds[INSTRUCTION_PTR] = None

      if op == self.ACC:
        ACCUMULATOR += arg
        INSTRUCTION_PTR += 1
      elif op == self.JMP:
        INSTRUCTION_PTR += arg
      elif op == self.NOP:
        logger.log(f"NOOP -> {INSTRUCTION_PTR}", "INFO")
        INSTRUCTION_PTR += 1
      else:
        raise Exception("Unknown Operation Type")

  def parse_cmd(self, cmd):
    logger.log(f"Parsing: [{cmd.strip()}]")
    (op, arg) = cmd.strip().split(" ")

    if op == "acc":
      parsed_op = self.ACC
    elif op == "jmp":
      parsed_op = self.JMP
    elif op == "nop":
      parsed_op = self.NOP
    else:
      raise Exception("Unknown Operation Type")

    return (parsed_op, int(arg))

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
  PART_PARSER = Accumulator(INPUT_FILE)
  PART_PARSER.run()


if __name__ == '__main__':
  main()

