







if __name__ == "__main__":
    sequence  = "mississippi"
    if len(sequence % 3 == 1):
        sequence = sequence+"$"
    elif len(sequence % 3 == 2):
        sequence = sequence+"$$"
    for alph in sequence:
