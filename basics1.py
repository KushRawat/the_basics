def func(*args):
    for x in args:
        x.upper()
        return args
print(func("asd", "ef"))