
def mergeSortedLists(l1,l2):
    mergedList = []
    s = min(len(l1),len(l2))
    b = max(len(l1),len(l2))

    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            mergedList.append(l1.pop(0))
        elif l2[0] < l1[0]:
            mergedList.append(l2.pop(0))
        else:
            mergedList.append(l1.pop(0))
            mergedList.append(l2.pop(0))


    mergedList += l1
    mergedList += l2

    return mergedList
