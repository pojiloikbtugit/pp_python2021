import re
s = input()
args = re.split("[.,]",s)
for x in args:
    if x:
        print(x)