import re 

file = open('raw.txt', 'r',encoding="utf8")
text = file.read()

BINPattern= r'\nБИН.*(?P<BIN>\b[0-9]+)'
NDSPattern= r'\nНДС Серия.*(?P<NDS>\b[0-9]+)'

BINtext=re.search(BINPattern,text).group("BIN")
NDStext=re.search(NDSPattern,text).group("NDS")

print(BINtext)
print(NDStext)


file.close()

