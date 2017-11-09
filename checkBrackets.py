def checkBrackets(code):
    openers_to_closers = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }

    openers = frozenset(openers_to_closers.keys())
    closers = frozenset(openers_to_closers.values())

    open_stack = []
    
    for char in code:
        if char in openers:
            open_stack.append(char)
        elif char in closers:
            last_opener = open_stack.pop()

            if char != openers_to_closers[last_opener]:
                return False
    
    return True        
