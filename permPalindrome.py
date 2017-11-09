def perm_palindrome(word):
    	
    d = dict() 
    for c in word:
        d[c] = d.get(c, 0) + 1
        
    numOdd = 0
    for k in d.keys():
        if d[k] % 2 != 0:
            numOdd += 1

    return (numOdd < 2)