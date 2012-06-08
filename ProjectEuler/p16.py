import math, sys

def sumdigits(num):
  sum = 0
  for n in str(num):
    sum += int(n)
  return sum

print sumdigits(int(math.pow(2, 1000)))
