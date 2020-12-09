#!/usr/bin/env python3

import sys
import re

from advent import LOG
from advent import AdventInputFileParser
from advent import AdventLineParser
from advent import AdventLogger
from advent import AdventParsedLineSummarizer

LOG_LEVEL = "INFO"
logger = AdventLogger(LOG_LEVEL)

#-------------------------------------------------------------------------------
# Part #1: LineParser Subclass
#-------------------------------------------------------------------------------
class Accumulator():

  ACC = 100
  JMP = 200
  NOP = 300

  def run(self, cmds):
    INSTRUCTION_PTR = 0
    ACCUMULATOR = 0

    while True:
      try:
        curr_cmd = cmds[INSTRUCTION_PTR]
      # IndexError indicates successful program completion
      except IndexError as ie:
        return ACCUMULATOR, True
      logger.log(f"INSTRUCTION_PTR -> {INSTRUCTION_PTR}")

      # None value indicates command already has been executed so return accumulator value
      if curr_cmd == None:
        return ACCUMULATOR, False

      (op, arg) = self.parse_cmd(curr_cmd)
      logger.log(f"PARSED: [{op}, {arg}]")
      #logger.log(f"accumulator={ACCUMULATOR}, instruction_ptr={INSTRUCTION_PTR}", "INFO")
      logger.log(f"accumulator={ACCUMULATOR}, instruction_ptr={INSTRUCTION_PTR}")
      logger.log("\n")

      # Mark command as having been done (before we increment instruction ptr below)
      cmds[INSTRUCTION_PTR] = None

      if op == self.ACC:
        ACCUMULATOR += arg
        INSTRUCTION_PTR += 1
      elif op == self.JMP:
        INSTRUCTION_PTR += arg
      elif op == self.NOP:
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
def find_bad_commands(cmds, accumulator):

  nop_jmp_indexes = [i for i,cmd in enumerate(cmds) if "nop" in cmd or "jmp" in cmd]

  print(nop_jmp_indexes)
  for i in range(0, len(nop_jmp_indexes)):
    tmp_cmds = cmds.copy()
    cmd_index = nop_jmp_indexes[i]

    logger.log(f"cmd_index={cmd_index}, cmds[0]={cmds[cmd_index]}", "INFO")

    orig = tmp_cmds[cmd_index]
    if "nop" in tmp_cmds[cmd_index]:
      tmp_cmds[cmd_index] = tmp_cmds[cmd_index].replace("nop", "jmp")
    else:
      tmp_cmds[cmd_index] = tmp_cmds[cmd_index].replace("jmp", "nop")
    replaced = tmp_cmds[cmd_index]
    logger.log(f"Replaced -> {orig} with -> {replaced}", "INFO")

    # total, was_success = accumulator.run(tmp_cmds)
    total, was_success = accumulator.run(tmp_cmds)

    print(was_success)
    if not was_success:
      print(f"RETURNED -> [{total}]")
    else:
      print(f"SUCCESSFUL Completion - Final Accumulator -> [{total}]")
      break

def load_commands(input_file):
  cmds = []
  with open(input_file) as input:
    cmds = input.readlines()
  return cmds

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

  accumulator = Accumulator()
  commands = load_commands(INPUT_FILE)
  if part_to_run == "1":
    result = accumulator.run(commands)
    print(f"RESULT: [{result}]")

  if part_to_run == "2":
    find_bad_commands(commands, accumulator)

if __name__ == '__main__':
  main()

