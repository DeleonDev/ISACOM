

def segment_options():
    with open('optionfiles/segmentos.txt') as f:
        d = list(x.rstrip().split(None, 1) for x in f)
    return d