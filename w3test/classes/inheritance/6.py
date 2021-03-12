class Person:
    def __init__(self,fname,lname):
        print('parent`s constructor')
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname,year):
        print('child`s constructor')
        super().__init__(fname,lname)
        self.graduationyear=year
    def printyear(self):
        print(self.graduationyear)
        

x= Student('John', 'Doe',2019)
x.printname()
x.printyear()
