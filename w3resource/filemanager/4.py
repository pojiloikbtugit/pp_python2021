f=open('input.txt','r')
l=f.readlines()

n=int(input())
for x in range(len(l)-n,len(l)):
 print(l[x])