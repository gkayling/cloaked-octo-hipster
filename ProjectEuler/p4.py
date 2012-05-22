import math

def isPalindrome(num):
  strnum = str(num)
  for i in range(0, int(math.floor(len(strnum)/2))):
    if strnum[i] != strnum[-(i+1)]: 
      return False
  return True

largest = 0
for i in range(100, 999):
  for j in range(100, 999):
    product = i*j
    if product > largest and isPalindrome(product):
      largest = product
print largest
