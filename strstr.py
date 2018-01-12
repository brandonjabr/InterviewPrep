def strStr(haystack, needle):
        
        n = len(needle)
        h = len(haystack)
        if haystack == needle:
            return 0
        elif n > h:
            return -1

        for i in range(0,h-n):
            currWord = haystack[i:i+n]
            if currWord == needle:
                return i
        return -1
                


h = "bbaabbbbbaabbaabbbbbbabbbabaabbbabbabbbbababbbabbabaaababbbaabaaaba"
n = "babaaa"

print strStr2(h,n)
