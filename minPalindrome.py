def solve(A):
    out = 0
    while A != A[::-1]:
        A = A[:len(A)-1]
        out += 1
    return out

solve('AACECAAAA')