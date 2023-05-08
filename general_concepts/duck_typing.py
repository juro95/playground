# In duck typing we don't check the type of the object, we check if the object has the required methods or not.
# If the object has the required methods then we can use it.

class Duck:
    def quack(self):
        print("Quack, quack")

    def fly(self):
        print("Flap, Flap")


class Person:
    def quack(self):
        print("I am quacking like a duck")

    def fly(self):
        print("I am flapping my arms")

class Fish:
    def swim(self):
        print("I am swimming")


def quack_and_fly(thing):
    thing.quack()
    thing.fly()

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

f = Fish()
quack_and_fly(f)

# We can see that the quack_and_fly function works with different data types and that the result is different
# depending on the data inputs.
# This is an example of duck typing in Python.
# We don't check the type of the object, we check if the object has the required methods or not.
# If the object has the required methods then we can use it.

# In structural typing we check if the object has the required methods and attributes during compile time.
# The main difference between duck typing and structural typing is that in duck typing we check if the object has the required methods during runtime. In
# structural typing we check if the object has the required methods during compile time so eg in typescript we would
# get an error if we try to use an object that doesn't have the required methods.