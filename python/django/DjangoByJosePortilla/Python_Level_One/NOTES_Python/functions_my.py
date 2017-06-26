def my_function(param1='default'):
    """
    THIS IS A DOCSTRING
    """
    print('my first python function! {}'.format(param1))
my_function()
my_function("somethign else")

def hello():
    return 'hello'
result = hello()
print(result)

#### Common problem with types and how to fix
def add_Num(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:
        return "Sorry, I need integers!"
added_Nums = add_Num(2,5)
print(added_Nums)
### If user accidentally mistakenly used "" and made strings, then
### without a type check, you would get:
### add_Num("2","5") would result in 25
## NOW if I do that:
added_Nums = add_Num("3", "7")
print(added_Nums)


### LAMBDA Expression

# Filter
mylist = [1,2,3,4,5,6,7,8]
def even_bool(num):
    return num%2 == 0

evens = filter(even_bool, mylist)
print(evens)
## filter() is a generator object like range and won't actually
## create a list unless you tell it to
print(list(evens))
        ### Instead of all of the above, you can use a lambda expression

odds = filter(lambda num:num%2 != 0, mylist)
print(list(odds))

## the "in" operator

print('x' in [1,2,3,4]) # returns false
print('x' in [1,2,'x',4,5]) # returns true
