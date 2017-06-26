###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
pick3 = list(digits[:3])
# pick3 = [1,2,3]
score = 0
guess = input("Try to guess the 3 digit number! All digits must be a different number. ")

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!

### MY SOLUTION ###
def checkMatch(nums):
    if nums == 'quit':
        print("Game Over. You quit!")
        return True
    count = 0
    close_count = 0
    num_list = list((int(x) for x in nums)) # using list comprehension an convert to int()
    if num_list == pick3:
        print("You got a PERFECT MATHC!!!")
        return True
    elif len(num_list) == 3:
        for i, value in enumerate(num_list):
            if num_list[i] == pick3[i]:
                count += 1
            elif value in pick3:
                close_count += 1
        print("You have {a} correct number(s) in the right spot, and {b} correct number(s) in the wrong spot.".format(a=count, b=close_count))
    else:
        print("Sorry, must be 3 digits. ")
        return False

while checkMatch(guess) != True:
    score += 1
    guess = input("Go again! Pick another 3 digit number. ")
    print("Current Score: ", score)

# mylist = [1,2,3,4]
# otherList = [4,5,6,7,3]
# for indx, value in enumerate(mylist):
#     print(any(x == value for x in otherList))
