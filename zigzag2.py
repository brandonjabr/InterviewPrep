def convert(A, B):
    
    rows = [[] for i in range(B)]
    asc = False
    currRow = 0
    for c in A:
        rows[currRow].append(c)
        if currRow == B-1:
            asc = True
        if currRow == 0:
            asc = False
        currRow = currRow + 1 if not asc else currRow - 1
        print currRow
    outStr = ''
    for row in rows:
        outStr += ''.join(row)
    return outStr

print convert("PAYPALISHIRING",3)