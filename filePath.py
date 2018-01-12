dir1 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

def longestFilePath(directory):
    paths = directory.split('\n')
    parents = {}
    filePaths = []
    longestPath = 0
    for i in range(len(paths)):
        el = paths[i]
        level = el.count('\t')
        name = el.replace('\t','')

        if '.' not in el:
            parents[level+1] = name + '/'
        else:
            
            fp = name
            
            while level > 0:
                fp = parents[level] + fp
                level -= 1

            filePaths.append(fp)
            if len(fp) > longestPath:
                longestPath = len(fp)
    return longestPath
            
print longestFilePath(dir1)