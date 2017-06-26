# LISTS
num_list = [1,2,3]
second_list = ['something', 'other', 'words', num_list]
print(len(second_list))

letter_list = ['a','b','c']
print(letter_list[-1]) # should print c
print(letter_list[:2]) # should print ab

# NOTE: UNLIKE strings, lists are mutable, meaning they can be changed
# after they were created.
# EXAMPLE:
letter_list[0] = 'z'
print(letter_list)

# how to add a new item to the end of a list: .append('new item')
# NOTE: you can append a list, but it will be that list all together
# as one item. If you want to append items individually by providing
# a list, then you have to use .extend()
# EXAMPLE:
letter_list.append(num_list) # you can add one item, list, element, or otherwise (object?)
print(letter_list)
letter_list.extend(num_list)
print(letter_list)


# REMOVING FROM A LIST

item = letter_list.pop()    # .pop() removes the last index item on a list
item_at_i_2 = letter_list.pop(2)    # .pop(index position) removes the item at the specified index position
print(letter_list)
print(item)
print(item_at_i_2)

# REVERSING A LIST
letter_list.reverse()
print(letter_list)

# SORTING A LIST
birth_dates_list = [54,25,67,49,51,11,82,79]
birth_dates_list.sort()
print(birth_dates_list)

# NESTED LISTS and LIST COMPREHENSION
nested_list = [1,2,['x','y','z'],3]
print(nested_list[2][1]) # should print y

# LIST COMPREHENSION
    # this prints 1,4,7
    # so it basically sets up a table (think connect four game)
    # we made a column of all the first index positions
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)
