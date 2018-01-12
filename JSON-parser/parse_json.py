
import re

class JsonObject:
    def __repr__(self):
        return self.tree.__repr__()

    def __init__(self, tokens):
        self.tree = parsejson(tokens)

    def __contains__(self, key):
        keyarray = key.split('.')
        tree = self.tree
        for key in keyarray:
            if key not in tree:
                return False
            tree = tree[key]

        return True

    def __getitem__(self, key):
        keyarray = key.split('.')
        tree = self.tree[keyarray.pop(0)]
        while keyarray:
            tree = tree[keyarray.pop(0)] 
        return tree
    
def isopenobject(token):
    return token == '{'

def iscloseobject(token):
    return token == '}'

def parsejson(tokens):
    token = tokens.pop(0)

    if isopenobject(token):
        json = {}
        while not iscloseobject(tokens[0]):
            key = parsejson(tokens)[1 : -1]
            value = parsejson(tokens)
            json[key] = value
        tokens.pop(0)
        return json

    return token

def parse_statement(smt):
    c,q = str(smt).strip().split(' ')
    pattern = re.compile(
            """{
            | ".*?"
            | [-+]?\d+
            | true
            | false
            | null
            | }
            (?x)""")
    tokens = pattern.findall(q)
    return tokens

# ------- Testing -------

in1 = 'add {"id":1,"last":"Doe","first":"John","location":{"city":"Oakland","state":"CA","postalCode":"94607"},"active":true}'
in2 = 'add {"type":"list","list":[1,2,3,4]}'

t1 = parse_statement(in1)
j1 = JsonObject(t1)

t2 = parse_statement(in2)
j2 = JsonObject(t2)

for _ in range(1):
    key = re.findall('\S+', str(input()))[0]
    print(j1[key] if key in j1 else 'null')
