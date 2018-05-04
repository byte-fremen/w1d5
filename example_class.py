# class Pet:
#     eyes = 2
#     legs = 4
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("You got a new pet")
#     def jump(self):
#         print("your pet is jumping")
#     def speak(self):
#         print('we are in the speak class')

# class Dog(Pet):
#     def __init__(self,name, age, fluffy):
#         # super().__init__(name, age)
#         Pet.__init__(self, name, age)
#         self.fluffy = fluffy

#     def speak(self):
#         print("Bark Bark")

# class Cat(Pet):
#     eyes = 1
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def speak(self):
#         return "Meow"

# class Bird(Pet):
#     legs = 2
#     def flying(self):
#         print("we are flying")


# shadow = Dog(name = "Shadow", age = 17, fluffy = "yes")
# lucy = Cat(name = "Lucy", age = 13)
# flappy = Bird("Tweety", 2)

# shadow.eyes
# lucy.legs
# shadow.speak()
# print(lucy.speak())





class Vehicle:
    wheels = 4
    terrain = "road"
    def __init__(self, color, make, model, year):
        self.color = color
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        return("you've started your {}".format(self.model))

class Car(Vehicle):
    
    def two_door(self):
        return('you drive a2 door?')

class Motorcycle(Vehicle):
    wheels = 2
    def drive(self):
        return("be careful out there")

class Truck(Vehicle):
    wheels = 16

    def honk(self):
        return "Honk Honk"

bryans_ride = Motorcycle("orange", "harley", "01", 1967 )
jasons_ride = Car("red", "mazda", "protege", 1991 )
josh_ride = Truck("black", "dodge", "durango", 1999 )














# class Vehicle:

#   def __init__(self, wheels, make, model, year):
#     self.wheels = wheels
#     self.make = make
#     self.model = model
#     self.year = year

#   def drive(self):
#     print("You're driving!")


# class Car(Vehicle):

#   def __init__(self, wheels, make, model, year):
#     Vehicle.__init__(self, wheels, make, model, year)

#   def interstate(self):
#     print("You are driving in your {year} {make} {model}.".format(year = self.year, make=self.make, model=self.model))


# class Motorcycle(Vehicle):

#   def __init__(self, wheels, make, model, year):
#     Vehicle.__init__(self, wheels, make, model, year)

#   def highway(self):
#     print("Your Motorcycle has {wheels} wheels.".format(wheels = self.wheels))

# class Truck(Vehicle):

#   def __init__(self, wheels, make, model, year ):
#     Vehicle.__init__(self, wheels, make, model, year)

#   def farm(self):
#     print("You've got sheep in the bed of your {make} {model}.".format(make = self.make, model = self.model))


# pt_cruiser = Car(wheels = 4, make = "Chrysler", model = "PT Cruiser", year = 2003)
# triumph = Motorcycle(wheels = 2, make = "Triumph", model = "Victory", year = 2006)
# ford_truck = Truck(wheels = 4, make = "Ford", model= "F350", year = 2001)























