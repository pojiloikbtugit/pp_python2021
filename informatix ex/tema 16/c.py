s=set(input().split())
s2=set(input().split())
intersec= s.intersection(s2)
print(*sorted(intersec))