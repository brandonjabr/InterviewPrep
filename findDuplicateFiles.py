
def findDuplicates(fileList):
    fileDict = {}
    filePairs = []

    for f in fileList:
        h = hash(f)
        if fileDict.has_key(h):
            filePairs.append((f,fileDict[h]))
        else:
            fileDict[h] = f
    return filePairs