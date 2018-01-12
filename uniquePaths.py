def uniquePaths(A, B):

    paths = 0
    visited = [(1, 1)]
    while len(visited) >= 1:
        path = visited.pop()
        if path[0] == A or path[1] == B:
            paths += 1
            continue
        if path[0] < A:
            down = (path[0] + 1, path[1])
            if down == (A, B):
                paths += 1
            else:
                visited.append(down)
        if path[1] < B:
            right = (path[0], path[1] + 1)
            if right == (A, B):
                paths += 1
            else:
                visited.append(right)
    return paths

print uniquePaths(15,12)