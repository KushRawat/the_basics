def mean(*args): # args is used as a parameter with the power of processing as many arguments as we want, and returns type of tuple
    print (args)
    print (type(args))
    print(sum(args))

#print(mean(1, 2, 3, 4, "a"))
print(mean(1, 2, 3, 4))
print(mean(1, 2, x = 3, 4)) # keyword argumetn will not work heree
