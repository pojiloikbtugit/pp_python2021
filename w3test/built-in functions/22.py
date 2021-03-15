class Person:
    name='Bob'
    age = 11 
    country = 'Bababooye'
x=getattr(Person,'page','my message')
print(x)