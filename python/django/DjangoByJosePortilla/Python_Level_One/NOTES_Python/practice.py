list1 = [1,4,5,8,9]
list2 = [6,4,7,3,8]
list3 = []

# for x in list1:
#     if x in list2:
#         print("CLOSE:")

# with list comprehension also using any()
if any([x for x in list1 if x in list2]):
    print("close!")
