def condition(x):
    if x > 7:
        return "WArm"
    else: 
        return "cold"

user_input = int(input("Enter temperature:"))
print(condition(user_input))