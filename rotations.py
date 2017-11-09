def get_rotations(s):
    rotations = [s]
    for i in len(s):
        rotations.append(rotate(s))
    return rotations



def rotate(s):
    return s[-n:] + s[:-n]