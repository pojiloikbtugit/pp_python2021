class Person:
    def __init__(self,fname,lname):
        print('parent`s constructor')
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        print('child`s constructor')
        super().__init__(fname,lname)
        

x= Student('John', 'Doe')
x.printname()
