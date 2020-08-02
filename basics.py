
with open("fruits.txt") as myfile: #myfile is th variable, with and open are methods
    content = myfile.read()
# with the ending of this block the file closes on its own
print(content)