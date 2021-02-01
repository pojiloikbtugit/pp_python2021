x = int(input())
num = int(input())
if x<=num:
  for i in range(x, num + 1):
     print(i)
elif x>=num:
    for i in range(x,num-1,-1):
      print(i)