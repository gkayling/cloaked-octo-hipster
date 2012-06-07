import math

def getC(a, b):
  return math.sqrt(a**2 + b**2)

for a in range(1, 500):
  for b in range(a, 500):
    c = getC(a, b)
    if a + b + c == 1000:
      print int(a * b * c)
      break
