# STRINGS

# BASICS
mystring = 'abcdefg'

# SLICING
# to "slice" you pick your starting index
# if you want to go all the way to the end, just leave right side of colon open
print(mystring[2:])

# slicing starting from beginning and ending at a specific index
# in Python, the slice ends going UP TO the index listed on the right of ":"
print(mystring[:3])

# prediction: this will print cde
print(mystring[2:5]) # CORRECT

# if you want to grab the entire string ---
print(mystring[:])

# you can add a second colon and put the "step size" which
# basically tells it how many index positions to skip
# this would print from beginning to end, but only printing every other one
print(mystring[::2])

# every 3:
print(mystring[::3] + " : This was every third index.")

# NOTE: Strings are immutable, meaning once defined you can't go back and
# change their definition
# EXAMPLE:
# mystring[0] = 'X'   # this will result in an error

# BASIC METHODS
x = mystring.upper()
y = mystring.lower()
c = mystring.capitalize()
print(x + " " + y + " " + c)

        # split method creates a list, and splits the string up
        # into elements based on the split requirement. NOTE: The default
        # is ' ', but you can change it to anything.
another_String = 'hello fine sir'
split_1 = another_String.split()
split_2 = another_String.split('e')
print(split_1) # gets rid fo spaces and makes an array
print(split_2) # gets rid of e and makes an array

# Print Formatting
# STRING INTERPOLATION

first_example = "Insert another string here: {}".format("INSERT ME!")
print(first_example)

first_example.format("Will this insert at the end too?") # this does nothing because you need the {}
print(first_example)

second_example = "Item one: {}  Item two: {}".format("dog", "cat")

# the nice thing with .format is that you can assign them a variable, and
# you can define the order they are placed in the string
second_example = "Item one: {ca}  Item two: {d}".format(d = "dog", ca = "cat")
print(second_example + "::: Do these variables have a global scope?")# + ca) --> nope, seems to stay local
