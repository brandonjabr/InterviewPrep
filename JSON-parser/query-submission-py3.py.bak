from __future__ import unicode_literals
import json
import csv
from collections import OrderedDict
import sys
import cProfile,pstats

class JSONQueryTable:

    def __init__(self):
        self.docs = []
        self.lists = []

    def sublistExists(self,l1,l2):
        occ = [i for i, a in enumerate(l1) if a == l2[0]]
        for b in occ:
            if l1[b:b + len(l2)] == l2:
                return True
            if len(occ) - 1 == occ.index(b):
                return False

    def comp_dict(self, a, b):
        for k, v in b.iteritems():
            if k not in a:
                return False
            elif type(v) == OrderedDict or type(v) == dict:
                if not self.comp_dict(a[k],v):
                    return False
            else:
                if a[k] != v:
                    return False
        return True
            
    def lookup_docs(self, query, delete=False):
        del_idxs = []
        for i in range(len(self.docs)):
            orig_doc,row = self.docs[i]
            for k, v in query.iteritems():
                if k not in row:
                    break
                if type(v) == OrderedDict or type(v) == dict:
                    if not self.comp_dict(row[k],v):
                        break  
                elif type(v) == list:
                    if not set(v).issubset(row[k]):
                        break  
                else:
                    if row[k] != v:
                        break
            else:
                if delete:
                    del_idxs.append(i)
                else:
                    sys.stdout.write(orig_doc+'\n')
        if delete:
            for idx in reversed(del_idxs):
                del self.docs[idx]
            
    def add_doc(self, doc):
        self.docs.append(doc)

    def parse_statement(self, smt):
        parse_smt = str(smt).strip().split(' ', 1)
        command, doc = parse_smt[0], parse_smt[1]
        query = json.loads(doc, object_pairs_hook=OrderedDict)

        if command == 'add':
            self.add_doc((doc, query))
        elif command == 'get':
            self.lookup_docs(query)
        elif command == 'delete':
            self.lookup_docs(query, delete=True)
        else:
            raise ArgumentError

# ------- Testing -------


q1 = ['add {"id":1,"last":"Doe","first":"John","location":{"city":"Oakland","state":"CA","postalCode":"94607"},"active":true}',
      'add {"id":2,"last":"Doe","first":"Jane","location":{"city":"San Francisco","state":"CA","postalCode":"94105"},"active":true}',
      'add {"id":3,"last":"Black","first":"Jim","location":{"city":"Spokane","state":"WA","postalCode":"99207"},"active":true}',
      'add {"id":4,"last":"Frost","first":"Jack","location":{"city":"Seattle","state":"WA","postalCode":"98204"},"active":false}',
      'get {"location":{"state":"WA"},"active":true}',
      'get {"id":1}',
      'get {"active":true}',
      'delete {"active":true}',
      'get {}'] * 500

q2 = ['add {"type":"list","list":[1,2,3,4]}',
      'add {"type":"list","list":[2,3,4,5]}',
      'add {"type":"list","list":[3,4,5,6]}',
      'add {"type":"list","list":[4,5,6,7]}',
      'add {"type":"list","list":[5,6,7,8]}',
      'add {"type":"list","list":[6,7,8,9]}',
      'get {"type":"list","list":[1]}',
      'get {"type":"list","list":[3,4]}'] * 1000

q3 = ['add {"id":3, "last":"Black", "first":"Jim","location":{"city":"Spokane","state":"WA","postalCode":"99207","bio":{"gender":"male","age":"23"}},"active":true}',
      'get {"location":{"state":"WA","bio":{"age":"23"}}}']

pr = cProfile.Profile()

pr.enable()

a = JSONQueryTable()

for q in q2:
    a.parse_statement(q)

pr.disable()
# -------End timing -------

pr.print_stats()