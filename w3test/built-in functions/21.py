class Person:
    name='Bob'
    age = 11 
    country = 'Bababooye'
x=getattr(Person,'age')
print(x)