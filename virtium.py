# Print out in descending order the frequency of each integer.

import operator

l = ["5", "-2", "-10", "0", "-10"]
print l
count = {} 
for n in l:
  if n in count:
    count[n] = count[n] + 1
  else:
    count[n] = 1
sorted_x = sorted(count.iteritems(), key=operator.itemgetter(1), reverse=True)
for n in count:
  print n + ' : ' + str(count[n])
