import time     # BUILT IN LIBRARY (WRITTEN IN C LANG)
import os       # STANDARD LIBRARIES # USE SYS.PREFIX TO FIND (WRIITEN IN C AND PYTHON BOTH)
import pandas # third party library, it's written in python itself

while True:
    if os.path.exists("temps_today.csv"):
        # CREATING A DATA FRAME
        data = pandas.read_csv("temps_today.csv")    # method to access csv through pandas 
        print(data.mean()["st1"])      # using mean only for st1
    else:
        print("File does not exist.")
    time.sleep(3)

#pandas is a package, a bunch of modules, but can be still referred to as a library