name = input("Enter your name:")
surname = input("Enter your surname:")
when = "today"

#message = "Hello %s %s whats up %s" %(name, surname, when)
#message = f"Hello {name} {surname}, whats up {when}"
message = "Hello {} {}, whats up {}".format(name, surname, name)
print(message)

