def area(a, b= 7): # defualt parameter
    return a * b

print(area(a = 4)) # keyword arguments , no need to assign b 
print(area(5)) # non KEYWORD ARGUMENTS , no need to assign a or b 
print(area(a = 4, b = 10)) # b can be assigned different value
print(area(5, 7)) # non KEYWORD ARGUMENTS

def area(a = 5, b): # a defualt parameter cannot be before a non-default parameter
    return a * b