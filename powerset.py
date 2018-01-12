def powerset(s):
    n = len(s)
    masks = [1<<j for j in xrange(n)]
    for i in xrange(2**n):
        yield [s[j] for j in range(n) if (masks[j] & i)]



# Find all instances of string T using any subsequence of S
matches = 0
for el in powerset('rabbbbbbbbbbbbbbbbbbbbbbit'):
    if ''.join(el) == 'rabbit':
        matches += 1

print matches, 'instances of "rabbit" in "rabbbit"'