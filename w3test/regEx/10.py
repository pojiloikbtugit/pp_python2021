import re 

txt = "The rain in Spain falls mainly in the plain! alls"
x=re.findall("al{2}s",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match!")