# BOOLEANS
# True  / 1
# False / 0

# TUPLES
    # The main difference between tuples and lists are that tuples are immutable
    # meaning they can't be changed after they are made. You can only redefine
    # the whole thing. You can't change part of it, like an index value.
t = (1,2,3)
print(t[0])

t = ('a',True,123)
print(t)

# SETS
    # unordered collections of unique elements
    # a set only takes in one unique element, so if you try to put in 2 multiple
    # times, it will only keep one of them.
x = set()

x.add(1)
x.add(2)
x.add(2)
x.add(2)
x.add(56)
x.add(0.54)
print(x)

converted = set([1,1,1,1,3,3,3,56,56,56,78])
print(converted)
