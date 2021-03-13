import re 

file = open('raw.txt', 'r',encoding="utf8")
text = file.read()
'''
BINPattern= r'\nБИН.*(?P<BIN>\b[0-9]+)'
NDSPattern= r'\nНДС Серия.*(?P<NDS>\b[0-9]+)'

BINtext=re.search(BINPattern,text).group("BIN")
NDStext=re.search(NDSPattern,text).group("NDS")
'''
ItemPatternText=r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
ItemPattern=re.compile(ItemPatternText)

for m in re.finditer(ItemPattern,text):
    print(m.group("name")+ " " + m.group("count")+ m.group("price"))



file.close()