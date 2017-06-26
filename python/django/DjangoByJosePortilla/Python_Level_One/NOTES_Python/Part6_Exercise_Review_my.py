#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'
print(s[0])

# 'o'
print(s[-1])

# 'djan'
print(s[:4])

# 'jan'
print(s[1:4])

# 'go'
print(s[4:])

# Bonus: Use indexing to reverse the string
    # my hacked up solution
print(s[-1] + s[-2] + s[-3] + s[-4] + s[-5] + s[-6])
    # tricky solution, this uses the "step size" feature but does it in
    # a negative manner, which basically reverses the string. pretty cool
print(s[::-1])


###############
## Problem 2 ##
###############

# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
l[2][2] = 'goodbye'
print(l)

###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))

###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
# the way he's probably looking for:
print("Hello my dog's name is {} and he is {} years old.".format("Sammy", 4))

#my fun version using the given variables, we had to add the variables into the .format()
# structure, so even "global" variables can't be used unless defined specifically
phrase = "Hello my dog's name is {name} and he is {age} years old.".format(age = age, name = name)
print(phrase)
