import math, datetime

def isPrime(num):
  if num == 2:
    return True
  for i in range(2, int(math.floor(math.sqrt(num))) + 2):
    if num % i == 0:
      return False
  return True

start = datetime.datetime.now()

sum = 0
for i in range(2, 2000000):
  if isPrime(i):
    sum += i

print sum

end = datetime.datetime.now()
diff = end-start
print 'Duration: ' + str(diff)
