#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
    for i, n in enumerate(nums):
        if (i + 2) < len(nums):
            if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
                return True
    return False
num_list1 = [1,2,5]
num_list2 = [5,3,1,2,3,5,7]
num_list3 = [4,4,3,3,2,2,1,1]
num_list4 = [1,1,2,2,3,3,4,4,5,5]

print(arrayCheck(num_list1))    # should be False
print(arrayCheck(num_list2))    # should be True
print(arrayCheck(num_list3))    # should be False
print(arrayCheck(num_list4))    # should be False

#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(str):
  return str[::2]

print(stringBits("Super Computer")) # should print: SprCmue

#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
    i = 0
    long_str_end = ''
    if len(a) <= len(b):
        while i < len(a):
            add_to_string = b[-len(a)+i]
            long_str_end += add_to_string
            i += 1
        if a.lower() == long_str_end.lower():
            return True
        else:
            return False
    elif len(a) >= len(b):
        while i < len(b):
            add_to_string = a[-len(b)+i]
            long_str_end += add_to_string
            i += 1
        if b.lower() == long_str_end.lower():
            return True
        else:
            return False

print(end_other("hello", 'hello goodbye')) # should return False
print(end_other('hello', 'goodbye hello')) # should return True
print(end_other('abc', 'xyzabc')) # should return True
print(end_other('abcdeflmnop', 'lmnop')) # should return True
print(end_other('abcd', 'qrxbcd')) # should return False because 'a' is missing
print(end_other('AbC', 'HiaBc')) # should return True


#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
    dub_Str = ''
    for char in str:
        add_char = char
        dub_Str += char + add_char
    return dub_Str

print(doubleChar("hello"))
print(doubleChar('AAbcCddEEf'))
print(doubleChar('Hi-There'))


#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    teen_range = list(range(13,20))
    if n != 15 and n != 16:
        for num in teen_range:
            if n == num:
                return 0
    return n


print(no_teen_sum(1, 2, 3)) # should be 6
print(no_teen_sum(2, 13, 1)) # should be 3
print(no_teen_sum(2, 1, 17)) # should be 3
print(no_teen_sum(55,15,14)) # should be 70

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    count = 0
    for i in nums:
        if i%2 == 0:
            count += 1
    return count

print(count_evens([2, 1, 2, 3, 4])) # should be 3
print(count_evens([2, 2, 0])) # should be 3
print(count_evens([1, 3, 5])) # should be 0
print(count_evens([2,42,5,6,7,8,8,8,22,53,77])) # should be 7
