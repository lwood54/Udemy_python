import re ## imports regular expressions module

patterns = ['term1', 'term2']

text = "This is a string with term1, but not the other!"

# for pattern in patterns:
#     print("I'm searching for: "+pattern)
#
#     if re.search(pattern,text):
#         print("MATCH!")
#     else:
#         print("NO MATCH!")

## re.search doesn't actually return a boolean, it returns a special search object
match = re.search('term1',text)

## returns <'_sre.SRE_Match'> (special regular expressions match object)
print(type(match))
print("Starts at index position: ",match.start()) # because it's an object, we can access its properties

## regular expressions can also split a string on a particular pattern
split_term = '@'

email = 'user@gmail.com'

print(re.split(split_term,email))

##### YOU CAN find all the instances of a patter in a string
##### by using re.findall()

print(re.findall('match', 'test phrase match in middle'))# returns an index with 'match'
print(re.findall('match','test phrase match in match middle'))# returns ['match','match']
### So, you can do things like find the length of the list of all matches.

def multi_re_find(patterns, phrase):

    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n') # prints a new line

test_phrase = 'sdsd.sssddd..sdddsddd...dsds...dssssss...sddddd'
test_phrase2 = 'This is a string! But it has punctuation. How can we remove it?'
test_phrase3 = "This is a string with numbers 12312 and a symbol #hashtag."

test_patterns = ['sd*'] # I want to find an s that is followed by 0 or more d's
test_patterns2 = ['sd+'] # I want to find an s that is followed by 1 or more d's
test_patterns3 = ['sd?'] # I want to find an s that is followed by 0 or 1 d's
test_patterns4 = ['sd{3}'] # I want to find an s that is followed by {# I want} d's
test_patterns5 = ['sd{1,3}'] # I want to find an s that is followed by {#,or #} of d's
test_patterns6 = ['s[sd]+'] # I want to find where s is followed by one or more s's or
                            # one or more d's
test_patterns7 = ['[^!.?]+'] # I want to find and remove anything that follows these
                             # punctuation marks.
test_patterns8 = ['[a-z]+'] # I want to find all the cases of one or more isntances
                            # where there is a lowercase letter a-z
test_patterns9 = ['[A-Z]+'] # I want to find all the cases of one or more isntances
                            # where there is an uppercase letter A-Z
### The r is needed with python in order to be able to use the \ as the
### escape code in python. Because \ is the escape code, but needs its own
### escape code which I guess is putting the r in front of the string? (Still
### a little confused as to how that works.)
test_patterns10 = [r'\d+'] # I want all of the digits (numbers)
test_patterns11 = [r'\D+'] # I want all of the NONdigits
test_patterns12 = [r'\s+'] # I want all of the whitespace
test_patterns13 = [r'\S+'] # I want all of the NON whitespace
test_patterns14 = [r'\w+'] # I want all of the alpha numeric characters (letters & nums)
test_patterns15 = [r'\W+'] # I want all of the NON alpha numeric characters

multi_re_find(test_patterns15,test_phrase3)
