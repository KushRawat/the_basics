def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)   
    
    return the_mean

dictionary = {"kush" : 12, "rawat" : 23}
temperatures = [12,243,65]
print(mean(dictionary))
print(mean(temperatures))