# LOGICAL OPERATORS

# AND
(1 > 2) and (2 < 3)

# OR
(1 > 2) or (2 < 3)

# Myltiple logical operators
(1 == 2) or (2 == 3) or (4 == 4)

#### INDENTATION IS IMPORTANT IN PYTHON!!!

if 1 < 2:
    print('yes!')
    if 20 < 3:
        print('nope')

if 1 == 2:
    print('hello')
elif 3 == 3:
    print('elif ran')
else:
    print('last')

#### LOOPS ####
# iterating through a list
seq = [1,2,3,4,5,6]
for i in seq:
    print(i)

# iterating through a dictionary
    # REMEMBER dictionaries don't retain their order
d = {"Sam":1, "Frank":2, "Dan":3}
    # only prints the key
for i in d:
    print(i)

    # to print key and value
for i in d:
    print(i, d[i], "Can I also print a string?")

for i,j in d.items():   ### another approach from StackOverflow
    print(i, j)

## Iterating through a TUPLE
    # a list of tuples
mypairs = [(1,2),(3,4),(5,6)]
for item in mypairs:
    print(item)
# tuple unpacking
for t1,t2 in mypairs:
    print(t1)
    print(t2)
    print(t1,t2)

## WHILE LOOPS
i = 1
while i < 5:
    print("i is: {}".format(i))
    print("i is:",i)
    i += 1


## Range function
range_list = list(range(0,5))
print(range_list)
range_list2 = list(range(0,20,2)) ## the 2 adds an interval
print(range_list2)
    ### The really cool thing about range() is that it allows you to iterate through incredibly large numbers without taking up significant memory. It simply remembers the range, then generates the number as needed.
for item in range(10):
    print(item)


## LIST COMPREHENSION
# standard version:
x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)

print(out)
## Instead do this:
more_out = [num**3 for num in x]
print(more_out)
