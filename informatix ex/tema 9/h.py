
a=input().split()
m=1000
for i in range(len(a)):
    b=int(a[i])
    if b>0 and b<m:
        m=b
print(m)
        