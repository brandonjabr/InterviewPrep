def revStr(string):
    chars = []
    for s in string:
        chars.append(s)
    
    chars = reversed(chars)

    return ''.join(chars)
