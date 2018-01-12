# Hard AF!!!!!

def longestPalindrome(s):
    def expend(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

    ans = ''
    for i in xrange(len(s)):
        
        # odd case, like "aba"
        tmp = expend(s, i, i)
        if len(tmp) > len(ans):
            ans = tmp
        
        # even case, like "abba"
        tmp = expend(s, i, i+1)
        if len(tmp) > len(ans):
            ans = tmp
            
    return ans