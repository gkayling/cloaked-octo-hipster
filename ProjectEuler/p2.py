
def isEven(num):
  return num % 2 == 0

max = 4000000
sum = 0;
i = 1
ii = 1
while True:
  if ii > max: 
    break
  if isEven(ii):
    sum += ii
  tmp = ii
  ii = i + ii
  i = tmp
print sum
