import re
import collections


words = re.findall('\w+', open('hamlet.txt').read().lower())
wcHamlet = collections.Counter(words)

print wcHamlet.most_common(20)
