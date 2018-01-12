def query(o,qs):
    #print o,qs
    x = o
    for t in qs:
        if t not in x:
            return 'null'
        x = x[t]
    if isinstance(x,str):
        return '"'+x+'"'
    elif isinstance(x,bool):
        if x:
            return 'true'
        else:
            return 'false'
    elif isinstance(x,int):
        return x
    elif x is None:
        return 'null'
    else:
        raise ValueError
        
def parse_str(s):
    s = s.strip()
    assert(s[0] == '"')
    i = s.index('"',1)
    return (s[1:i],s[i+1:])

def parse_obj(s):
    s = s.strip()
    assert(s[0] == '{')
    o = dict()
    while s[0] != '}':
        assert(s[0] in ',{')
        s = s[1:].strip()
        key,s = parse_str(s)
        s = s.strip()
        assert(s[0] == ':')
        s = s[1:].strip()
        if s[0] == '{':
            v,s = parse_obj(s)
        elif s[0] == '"':
            v,s = parse_str(s)
        elif s[:4] == 'true':
            v = True
            s = s[4:]
        elif s[:5] == 'false':
            v = False
            s = s[5:]
        elif s[:4] == 'null':
            v = None
            s = s[4:]
        else:
            assert(s[0] in '+-0123456789')
            i = 0
            while s[i] in '+-0123456789':
                i += 1
            v,s = int(s[:i]),s[i:]
        o[key] = v
        s = s.strip()
    return (o,s[1:])

testJSON = '{ \
    "firstName": "John", \
    "lastName": "Smith", \
    "isAlive": true, \
    "age": 25, \
    "heightCm": "167.64", \
    "address": { \
        "streetAddress": "21 2nd Street", \
        "city": "New York", \
        "state": "NY", \
        "postalCode": "10021-3100", \
        "phone": null \
    } \
}\
firstName'


n,q = map(int,raw_input().split())
s = ''
for _ in range(n):
    s += raw_input()

o,s = parse_obj(s)
assert(s.strip()=="")

for _ in range(q):
    s = raw_input().strip()
    print query(o,s.split('.'))