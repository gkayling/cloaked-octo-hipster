max = 4000000
sum = 0;
i = 1
ii = 1
while True:
  i = i + ii
  if i > max: 
    break
  if i % 2 == 0:
    sum += i
  ii = ii + i
  if ii > max:
    break 
  if ii % 2 == 0:
    sum += ii
print sum
