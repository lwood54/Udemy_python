#### SCOPE (aka Namespace)

x = 25

def my_func():
    x = 50
    return x

# print(x)
# print(my_func())

## Scope in lambda
lambda x: x**2

# Enclosing function locals
name = 'This is a global name!'

def greet():
    name = "Sammy"

    def hello():
        print("hello " + name)
    hello()
# greet()


#################################################
        ####### OBJECT ORIENTED PROGRAMMING ##########
#################################################
class Sample():
    pass

x = Sample()
# print(type(x))  # returns  <class '_main_.Sample'>

class Dog():
    # CLASS OBJECT ATTRIBUTE:
    species = "mammal"

    # most basic method for an object, the "self" is required
    # this is an initialization funciton
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    

## How to define and call objects in Python:
mydog = Dog("Lab","Sammy")
other_dog = Dog("Huskie","Holly")
print(mydog.breed)
print(other_dog.name)
