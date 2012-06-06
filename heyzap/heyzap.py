import re

f = open('heyzap-example-log', 'r')
log = f.read()

pages = {'home':r'www.heyzap.com/]$', 'payments':r'www.heyzap.com/payments/]$', 'get_item':r'www.heyzap.com/payments/get_item'}
counts = {'home':0, 'payments':0, 'get_item':0, 'weebly':0}

weeblystuff = ['"embed_key"=>"12affbbace"', '"action"=>"index"', '"controller"=>"heyzap"']


homecount = 0
for line in iter(log.splitlines()):
  for key in pages:
    if re.search(pages[key], line) is not None:
      counts[key] += 1    
      break 
  if re.search('^  Parameters:', line) is not None:
    weebly = True
    for w in weeblystuff:
      if re.search(w, line) is None:
        weebly = False
        break
    if re.search('"permalink"=>""', line) is None and weebly is True:
      counts['weebly'] += 1
    
print counts
