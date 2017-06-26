### Decorators can be thought of as functions that modify the functionality
### of other functions. They really help make your code shorter and more
### 'pythonic'. They are used alot in Python web frameworks. Especially
### Django and Flask.

# s = "GLOBAL"
#
# def func():
#     mylocal = 10
#     print(locals()) ## returns a dictionary of local variables
#     print(globals()) ## returns a dictionary of global variables
#     print(globals()['s']) ## returns the value from the specific key 's'
# func()


# def hello(name="Logan"):
#     return "hello "+name
#
# print(hello())
#
# mynewgreet = hello
# print(mynewgreet())


# def hello(name="Logan"):
#     print("The hello() function has been run!")
#
#     def greet():
#         return "This string is inside greet()."
#
#     def welcome():
#         return "This string is inside welcome()!"
#
#     # print(greet())
#     # print(welcome())
#     # print("End of hello")
#     if name == "Logan": # if the name == Logan, then we return the whole function greet
#         return greet
#     else:
#         return welcome
#
# x = hello() # we set x = to what is returned by the hello() function
#
# print(x())
#
# def hello():
#     return "Hi Logan!"
#
# def other(func):
#     print("Hello")
#     print(func) # prints the whole function (func), not just the return of func
#     print(func()) # prints what is RETURNED by func() because() were added.
#
# other(hello)



############# CREATING A DECORATOR ############
def new_decorator(func):

    def wrap_func():
        print("Code here before executing func.")
        func()
        print("func() has been called.")

    return wrap_func

### LONG WAY ###
# def func_needs_decorator():
#     print("This function is in need of a decorator!")
#
# func_needs_decorator = new_decorator(func_needs_decorator)
#
# func_needs_decorator()
### END OF LONG WAY ###


### MORE EFFICIENT WAY OF USING DECORATOR FUNCTIONS ###
@new_decorator ## this passes listed function through "new_decorator" function
def func_needs_decorator():
    print("This function is in need of a decorator!")

func_needs_decorator()


## So basically:
## @new_decorator
##  is the equivalent to:
## func_needs_decorator = new_decorator(func_needs_decorator)

## helps with reassigning and passing functions. It's like saying:
####    assign func_needs_decorator to the return value of passing
####    new_decorator() with the argument of func_needs_decorator
