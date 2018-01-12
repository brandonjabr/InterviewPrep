def checkBrackets(code):
    match_dict = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }

    open_chars = frozenset(match_dict.keys())
    close_chars = frozenset(match_dict.values())

    open_stack = []
    
    for char in code:
        if char in open_chars:
            open_stack.append(char)
        elif char in close_chars:
            last_opener = open_stack.pop()

            if char != match_dict[last_opener]:
                return False
    
    return True        
