import math
a = float(input())
if math.ceil(a) - a <= 0.5:
 print(math.ceil(a))
else:
 print(math.ceil(a) -1)