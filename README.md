# Object Oriented Programming Day 2

### Learning Objectives
***Students Will Be Able To...***

* Utilize classes using Inheritance
* Use items from a parent class
* Use items from a child class
* Utilize the terminal to help research

---
### Context

* This is the last topic of object oriented programming.
* Inheritance allows us to organize our code every more regarding objects

---
### Lesson

#### Part 1 - OOP 5 min recap

* Yesterday we were introduced to the idea that everything in Python is an Object
* We wrote classes
* Instance Variables vs Instance methods
* Scope - LEGB

#### Part 2 - Inheritance

* Make a class Pet
* Make a class Dog
* Make a class Cat
* Make a class Bird

```
class Pet:
    eyes = 2
    legs = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("You got a new pet")

    def jump(self):
        print("your pet is jumping")

class Dog(Pet):

    def __init__(self,name, age, fluffy):
        Pet.__init__(self, name, age)
        self.fluffy = fluffy

    def speak(self):
        print("Bark Bark")

class Cat(Pet):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Meow")

shadow = Dog(name = "Shadow", age = 17, fluffy = "yes")

lucy = Cat(name = "Lucy", age = 13)

shadow.eyes
lucy.legs
shadow.speak()
lucy.speak()
```
* The local method takes precedent over the parent method
* Brought up in class: If all pets have a name and an age we can put it in the parents `init` method
    * To utilize the parent `init` method we could call it inside of the child's `init` method and pass the values through to the parent

***NOTE***

* In the above example, class Pet can be written like so:

```
class Pet(object):
```
* You may be familiar with this syntax if you did tutorials in python 2
* What this means is that `ALL` classes will be inheriting from the `Object` class

***Five Min Exercise***

* Make a parent class called `Vehicle`
* Make three child classes: `Car`, `Truck`, `Motorcycle`
* Instantiate the child classes
* Each child should have their own unique methods that will return an instance variable
* Each child should also have access to variables inside of the parent class

#### Part 3 - Best Practices

***Pseudo Code***

* Before writing any real code just make bullets of what is your goal, what is your endpoint, and how can you get there
* Plan out your app, what classes will you have, what methods will be inside of those classes

***PUDB***

* Install this using `pip3 install pudb`
* Run a file using pudb with `python3 -m pudb.run filename.py`
* GO THROUGH THE TUTORIAL BEFORE TRYING THIS ON YOUR OWN
* PUDB
    * You **must** debug systematically.
    * Here's an online tutorial: [http://heather.cs.ucdavis.edu/~matloff/pudb.html](http://heather.cs.ucdavis.edu/~matloff/pudb.html)

#### Other best practices
 
* Inside your terminal make use of 
	* help()
	* dir()
	* doc_strings = """ This Is A Doc String """
	* Open a file inside Python REPL using `-i`
		* `python3 -i my_file.py`

#### More complicated OOP concepts to checkout
 
 * Class methods vs. Static methods
 	* [Python Methods and How They Work](https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods)

```
class Blah:
	
```	
 
 * Look at the following code:
 
```
 class Base(object):
    def __init__(self):
        print "Base created"

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super().__init__()

ChildA()
ChildB()
```
* What's the difference? Research here: 
	* [http://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods](http://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods)
* `Class.__init__` vs. `def __init__` vs. super
	* [http://learnpythonthehardway.org/book/ex44.html](http://learnpythonthehardway.org/book/ex44.html)
    * [http://stackoverflow.com/questions/1173992/what-is-a-basic-example-of-single-inheritance-using-the-super-keyword-in-pytho](http://stackoverflow.com/questions/1173992/what-is-a-basic-example-of-single-inheritance-using-the-super-keyword-in-pytho)
- Checkout this usage of Super --> [http://i.imgur.com/SOniuXb.png](http://i.imgur.com/SOniuXb.png)
	