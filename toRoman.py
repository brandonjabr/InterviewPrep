def roman(A):
    roman = ''
    while A != 0:
        if A >= 1000:
            roman += 'M'
            A -= 1000
        elif A >= 500:
            roman += 'D'
            A -= 500
        elif A >= 100:
            roman += 'C'
            A -= 100
        elif A >= 50:
            roman += 'L'
            A -= 50
        elif A >= 10:
            roman += 'X'
            A -= 10
        elif A >= 5:
            roman += 'V'
            A -= 5
        else:
            roman += 'I'
            A -= 1
    return roman

print roman(1)
print roman(4)
print roman(12)
print roman(1500)
print roman(1234)