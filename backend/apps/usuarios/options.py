def gender_options():
    with open('gender.txt') as f:
        d = list(x.rstrip().split(None, 1) for x in f)
    return d