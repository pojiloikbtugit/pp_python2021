age = [4,7,7,12,21,16]
def myfunc(x):
    if x<18:
        return False
    else:
        return True
adults = filter(myfunc,age)
for x in adults:
    print(x)