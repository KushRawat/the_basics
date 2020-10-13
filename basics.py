import time
import os
import pandas # third party library, it's written in python itself

while True:
    if os.path.exists("temps_today.csv"):
        data = pandas.read_csv("temps_today.csv")    # method to access csv through pandas
        print(data.mean())      # using mean method
    else:
        print("File does not exist.")
    time.sleep(3)

#pandas is a package, a bunch of modules, but can be still referred to as a library