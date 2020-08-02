def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get) #kwargs.get Returns the value for key if key is in the dictionary, else default.
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))