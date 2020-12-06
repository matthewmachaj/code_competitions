#!/usr/bin/env python3

import sys

nums = []
with open('1.in') as input:
  line = input.readline().strip()
  while line:
    nums.append(int(line))
    line = input.readline().strip()

found = False
for i in nums:
  for j in nums:
    for k in nums:
      sum = i + j + k
      if sum == 2020:
        print(f"Sum found for i={i}, j={j}, k={k}")
        print(i * j * k)
        found = True
        sys.exit(0)
