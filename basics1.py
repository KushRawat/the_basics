def func(*args):
    args = [x.upper() for x in args]
    return sorted(args)