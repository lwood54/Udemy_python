try:
    f = open('simple.txt','r')
    f.write("Test write to simple text!")
# except IOError: # Stands for "Input/Output operation error"
## you can also take away a specific error and just have it do something
## with any error. Example:
except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    f.close()
finally:
    print("I always work no matter what.")

####### Carry out code without the try/except
# f = open('simple.txt', 'r')
# f.write('Test to see if this writes text!')
# print("hello world!")   ### this results in error, but also stops code
