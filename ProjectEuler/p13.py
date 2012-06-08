
f = open('p13.input', 'r')
x = 0
for n in iter(f.read().splitlines()):
  x += int(n)
print str(x)[:10]
