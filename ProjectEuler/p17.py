

u = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
numchars = 0
for i in range(1, 1001):
  num = '%(#)04d' % {'#' : i}
  string = ''
  if num[0] != '0':
    string += u[int(num[0])] + 'thousand' 
  if num[1] != '0':
    string += u[int(num[1])] + 'hundred'
    if num[2] != '0' or num[3] != '0':
      string += 'and'
  if int(num[2:]) >= 20:
    string += tens[int(num[2])] + u[int(num[3])]
  else:
    string += u[int(num[2:])]
  numchars += len(string)
print numchars
