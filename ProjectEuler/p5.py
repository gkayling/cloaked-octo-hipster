import datetime

def isDivisible(num, low, high):
  for i in range(high, low, -1):
    if num % i != 0:
      return False
  return True

high = 20
num = high
start = datetime.datetime.now()
while not isDivisible(num, 1, high):
  num += high
print num
end = datetime.datetime.now()

diff = end-start
print 'Duration: ' + str(diff)
