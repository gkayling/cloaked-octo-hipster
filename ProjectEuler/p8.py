
f = open('p8.input', 'r')
num = f.read().replace('\n', '')

highprod = 1 
prod = 1
numiter = 0
for i in range(0, len(num)):
  prod *= int(num[i])
  if numiter > 4:
    if prod > highprod:
      highprod = prod
    if int(num[i-4]) != 0:
      prod /= int(num[i-4])
    if prod == 0:
      hasZeros = False
      for j in range(i-4, i):
        if num[j] == '0':
          hasZeros = True
      if not hasZeros:
        prod = 1
        numiter = 0
  numiter += 1   
print highprod
