def find_sum(**kwargs):
    return sum(kwargs.values()) # method of calling value from keyword argument in case of **kwargs parameter in a function

print(find_sum(x = 9))