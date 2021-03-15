class Person:
  name='Bobik'
  age=40
setattr(Person,'age',40)
x=getattr(Person,'age')
p=Person()
print(p.age)