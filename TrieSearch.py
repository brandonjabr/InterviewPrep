import sys
for line in sys.stdin:
    print(line, end="")

class Trie:
    def __init__(self):
        self.root = {}

    def add_or_check_word(word):
        curr = self.root
        new_word = False
        
        for char in word:
            if char not in curr:
                new_word = True
                curr[char] = {}
            curr = curr[char]
        
        if 'END' not in curr:
            new_word = True
            curr['END'] = word
        
        return new_word
    
    def match_prefix(s):
        curr = self.root
        for char in s:
            if char in curr:
                curr = curr[char]
            else:
                return '<NONE>'
        return curr
    
    def get_matches(pref, d):
        i = 0
        for k in d.keys():
            curr = d[k]
            while 'END' not in curr:
                curr = curr[k]
            print curr['END']
            
            
