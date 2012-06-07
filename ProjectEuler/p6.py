import math

sums = 0;
sqsums = 0;
for i in range(1, 101):
  sums += i
  sqsums += i**2

print str(sums**2 - sqsums)
