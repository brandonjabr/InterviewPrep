def counting_sort(l,maxVal):
    inList = [0] * maxVal
    outList = []

    for val in l:
        inList[val] += 1
    
    for idx, count in enumerate(inList):
        outList += [idx]*count
    
    return outList