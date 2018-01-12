def subsequences(s,n):
	return map(lambda i: s[i:i+n], range(len(s)-n+1))
allSubs = []
for i in range(1,len('rabbbit')+1):
    allSubs += subsequences('rabbbit',i)

print allSubs