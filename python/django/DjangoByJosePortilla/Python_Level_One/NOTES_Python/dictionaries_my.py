# DICTIONARIES
# Dictionaries are very similar to objects in JS, they are flexible in the
# data types that can be stored
my_stuff = {
    "key1":"value",
    'key2':'value2',
    'key3': [1,2,3],
    'key4': {'subKey1':5}
}
print(my_stuff['key1'])
# to call values of dictionaries nested in other dictionaries
print(my_stuff['key4']['subKey1'])

more_stuff = {
    'lunch': 'pizza',
    'bfast': 'eggs'
}
print(more_stuff['lunch'])

# CHANGING A KEY : Value pair
more_stuff['lunch'] = 'burger'
print(more_stuff['lunch'])

# ADDING a new Key
more_stuff['dinner'] = 'gumbo'
print(more_stuff['dinner'])

# NOTE: Unlke JS, you can't add "methods" inside the dictionaries
# like how when you add a function in a JS object, that is a method
