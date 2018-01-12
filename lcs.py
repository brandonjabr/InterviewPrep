# For two strings (dynamic)
def lcs(s1, s2):
   m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
   longest, i_longest = 0, 0

   for i in xrange(1, 1 + len(s1)):
       for j in xrange(1, 1 + len(s2)):
           if s1[i - 1] == s2[j - 1]:
               m[i][j] = m[i - 1][j - 1] + 1
               if m[i][j] > longest:
                   longest = m[i][j]
                   i_longest = i
           else:
               m[i][j] = 0
   return s1[i_longest - longest: i_longest]

# For an array of strings
def longestCommonPrefix(self, A):
    if not A:
        return ""
    for i in xrange(len(A[0])):
        for string in A[1:]:
            if i >= len(string) or string[i] != A[0][i]:
                return A[0][:i]
    return A[0]