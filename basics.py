with open("fruits.txt", "a+") as myfile:    # usinf a+ to append and read at the same time otherwise we wont be able to read the file     # unlike "w", "x" does not overwrites file
    myfile.write("\nOkra") # to append on anew line
    myfile.seek(0)   # to bring cursor back to 0/top
    content = myfile.read()

print(content)