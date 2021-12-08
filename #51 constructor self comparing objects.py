"""class main_computer:
    def __init__(self):
        self.name ="rohith"
        self.age = 22
    def update(self):
        self.age = 20
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 =main_computer()
c2 =main_computer()
c1 .name,c1.age ="SHILPA",20
c2.update()
if c1.compare(c2):
    print("they are same")
else:
    print('they are different')

print(c1.name,c1.age)
print(c2.name,c2.age)
so __init__ is a constructor of variable we ca change a variable with pointing the
object"""
"""what is the use of self means the self variable store or pointing everything er stored
 and we can call what object we need to call the value"""
class mydetails:
    def __init__(self):
        self.name ="rohith"
        self.age = 22
    def update(self):
        self.age =23
        self.name = "shilpa"
    def compare(self,other):
        if self.age== other.age:
            return True
        else:
            return False
c1 = mydetails()
c2 = mydetails()
c1.update()
print(c1.name,c1.age)
print(c2.name,c2.age)
if c1.compare(c2):
    print("they are same")
else:
    print('they are different')




