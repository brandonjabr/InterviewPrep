def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    rowStrings = [''] * numRows
    currRow = 0
    ascending = False
    for char in s:

        rowStrings[currRow] += char

        if currRow == numRows-1:
            ascending = True
        elif currRow == 0:
            ascending = False

        currRow = currRow - 1 if ascending else currRow + 1

    outStr = ''
    for s in rowStrings:
        outStr += s

    return outStr
