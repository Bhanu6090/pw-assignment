# Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed
# and average_of_vehicle.
# Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
# Create a method named seating_capacity which takes capacity as an argument and returns the name of
# the vehicle and its seating capacity.
# Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.
# Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this
# class.
# Q5.What is method overriding in python? Write a python code to demonstrate method overriding.
class vehicle :
    def __init__(self,name_of_vehicle,max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed 
        self.average_of_vehicle = average_of_vehicle
class car(vehicle):
    def seating_capacity(self,capacity ):
        self.capacity = capacity 
        return [self.name_of_vehicle, self.capacity]
v1 = vehicle("truck ", 79, 2)
c1 = car("truck ", 79, 2)
print(c1.seating_capacity(4))
#Q3 
"""When a class is derived from more than one base class it is called multiple Inheritance. """
class grandfather:
    def decies(self):
        print("grand father has hair loss problem")
class grandmother :
    def deceasie(self):
        print("grand mother is dibatic patience")
class child(grandfather,grandmother):
    pass 
    
c1 = child()
c1.deceasie()
c1.decies()

class bank:
    def __init__(self,enrollment_no):
        self.__enrollment_no = enrollment_no
    def getter(self):
        return self.__enrollment_no
    def setter(self,enrollment_no):
        self.__enrollment_no = enrollment_no
b = bank("012464cd201015")
print(b.getter())
b.setter("0124vfd30176")
print(b.getter())

class lst(list):
    def pop(self):
        return super().pop() # overriding the method by using super()
l = lst()
l.append(0)
print(l.pop())
    

