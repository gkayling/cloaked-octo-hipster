import datetime
import math

def isPrime(num):
  if num == 2:
    return True
  for i in range(2, int(math.floor(math.sqrt(num))) + 2):
    if num % i == 0:
      return False
  return True

start = datetime.datetime.now()

numprimes = 0
num = 2 
while True:
  if isPrime(num):
    numprimes += 1
  if numprimes == 10001:
    break
  num += 1
print num

end = datetime.datetime.now()
diff = end-start
print 'Duration: ' + str(diff)
