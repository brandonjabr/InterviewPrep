def compare(x,y):
    a = int(str(x) + str(y))
    b = int(str(y) + str(x))
    return a - b

def largestNum(A):
    A = [str(num) for num in list(reversed(sorted(A,cmp=compare)))]
    return ''.join(A)

a = [3, 30, 34, 5, 9]