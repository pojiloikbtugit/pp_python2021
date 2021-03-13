import re 
txt = 'The rain in Spain'
txt2 = 'The Spain'
x=re.search("^The.+Spain$",txt2)

if x:
    print("YES!, We have a match!")
else: 
    print("No match!")