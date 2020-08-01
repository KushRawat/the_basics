def mean(**kwargs): # this is used when key words arguments need to be used ,args is used as a parameter with the power of processing as many arguments as we want, and returns type of tuple
    #print (args)
    #print (type(args))
    #print(sum(args))
    return kwargs
#print(mean(1, 2, 3, 4, "a"))
#print(mean(1, 2, 3, 4)) # willl not work
print(mean(a = 1, b = 2, x = 3, y = 4)) 