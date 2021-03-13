import re 
txt = 'The1233rain in Spain'

x=re.findall("[^0123]",txt)

print(x)