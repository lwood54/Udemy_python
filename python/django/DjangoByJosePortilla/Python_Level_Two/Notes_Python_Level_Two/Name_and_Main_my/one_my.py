def func():
    print("func() in one_my.py")

print("Top level one_my.py")

if __name__ == '__main__':
    print("one.py is being run directly")
else:
    print("one.py has been imported")
