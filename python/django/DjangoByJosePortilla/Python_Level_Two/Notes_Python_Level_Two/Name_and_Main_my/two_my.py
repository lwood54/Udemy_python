import one_my
print("Top level two_my.py")
one_my.func()

if __name__ == '__main__':
    print("Two.py being run diretly")
else:
    print("Two is being imported")
