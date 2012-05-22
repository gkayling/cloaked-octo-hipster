import math

number = 600851475143

def isPrime(num):
  for i in range(2, int(math.floor(math.sqrt(num)))):
    if num % i == 0:
      return False
  return True

bigprime = 1
for i in range(1,int(math.floor(math.sqrt(number)))):
  if number % i == 0 and isPrime(i):
    bigprime = i
print bigprime
