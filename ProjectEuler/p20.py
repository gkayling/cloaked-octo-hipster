
def factorial(n):
  if n == 1:
    return 1
  return n*factorial(n-1)

sum = 0
for s in str(factorial(100)):
  sum += int(s)

print sum
