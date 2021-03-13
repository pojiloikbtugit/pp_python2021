import re 

file = open('raw.txt', 'r',encoding="utf8")
text = file.read()

Pattern= r'\nБИН.*(?P<BIN>\b[0-9]+).*\nНДС Серия.*(?P<NDS>\b[0-9]+)'

x=re.compile(Pattern)

for match in x.finditer(text):
    print(match.group("BIN"))
    print(match.group("NDS"))

file.close()

