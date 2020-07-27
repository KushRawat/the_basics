temps = [221, 234, 53, 6345]

new_temp = [x if x != 53 else 0 for x in temps]

print(new_temp)