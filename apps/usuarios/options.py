def gender_options():
    with open('optionfiles/gender.txt') as f:
        d = list(x.rstrip().split(None, 1) for x in f)
    return d


def blood_type_options():
    with open('optionfiles/blood_type.txt') as f:
        d = list(x.rstrip().split(None, 1) for x in f)
    return d


def disability_options():
    with open('optionfiles/disability.txt') as f:
        d = list(x.rstrip().split(None, 1) for x in f)
    return d

def clasification_options():
    with open('optionfiles/clasification.txt') as f:
        d = list(x.rstrip().split(None, 1) for x in f)
    return d

def months_options():
    with open('optionfiles/months.txt') as f:
        d = list(x.rstrip().split(None, 1) for x in f)
    return d

def states_options():
    with open('optionfiles/states.txt') as f:
        d = list(x.rstrip().split(None, 1) for x in f)
    return d