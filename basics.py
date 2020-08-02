def find_sum(**kwargs):
    print (kwargs.keys()) # method of calling value from keyword argument in case of **kwargs parameter in a function
    return (kwargs.values())
print(find_sum(x = 9))

#returns a dictionary