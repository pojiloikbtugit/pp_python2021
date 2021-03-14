n= int(input())
d={}
for i in range(n):
    f,s = input().split()
    d[f]=s
    d[s]=f
print(d[input()])