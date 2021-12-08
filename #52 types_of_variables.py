"variables are classified into two type "
"1 = instance variable "
"2 = class variable or static variable "
"""instance variable is the one which is stored in __init__ function where
if we updta the value of the  variable it does not affect the pre stored avribale 
and if we want to call the variable we need to call object.variable name"""
"""class variable or static variable id the one which we not using any function to store the variable 
 we need to store inside the class we we need to change the variable we need to call the class.variable name = updated value
     examples are shown below"""


class car:
    wheel = 4
    def __init__(self):
        self.company ="bmw"
        self.cost = "8lakh"
        self.milage = "10kmpl"
my_car1 =car()
my_car2 =car()
my_car2.company="honda"
car.wheel=6
print(my_car1.company,my_car1.cost,my_car1.milage,my_car1.wheel)
print(my_car2.company,my_car2.cost,my_car2.milage,my_car2.wheel)









