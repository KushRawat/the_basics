with open("fruits.txt", "x") as myfile:     # unlike "w", "x" does not overwrites file
    myfile.write("Okra")