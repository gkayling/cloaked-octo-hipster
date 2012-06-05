# Find the power set of a list (not including the null set) 

import math

l = ['A', 'B', 'C', 'D', 'E']

for i in range(0, int(math.pow(2, len(l)))):
  vector = bin(i)[2:]
  vector = vector.zfill(len(l))
  word = []
  for j in range(0, len(vector)):
    if vector[j] == '1':
      word.append(l[j])
  print "".join(word)
