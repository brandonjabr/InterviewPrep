
""" -------------------------- Hash Table -------------------------- """

def hash_function(key_str, size):
    return sum([ord(c) for c in key_str]) % size


############ HashTable class
class HashTable:
    """ Hash table which uses strings for keys. Value can be any object. And it chains repeat key values in a list.
    Example usage:
        ht = HashTable(10)
        ht.set('a', 1).set('b', 2).set('c', 3)
        ht['c'] = 30
    """

    def __init__(self, capacity=1000):
        """ Capacity defaults to 1000. """

        self.capacity = capacity
        self.size = 0
        self._keys = []
        self.data = [[] for _ in range(capacity)]

    def _find_by_key(self, key, find_result_func):
        index = hash_function(key, self.capacity)
        bucket = self.data[index]
        found_item = None
        for item in bucket:
            if item[0] == key:
                found_item = item
                break

        return find_result_func(found_item, bucket)

    def set(self, key, obj):
        """ Insert object with key into hash table. If key already exists, then the object will be
        updated. Key must be a string. Returns self. """

        def find_result_func(found_item, bucket):
            if found_item:
                found_item.append(obj)
            else:
                bucket.append([key, obj])
                self.size += 1
                self._keys.append(key)

        self._find_by_key(key, find_result_func)
        return self

    def get(self, key):
        """ Get object with key (key must be a string). If not found, it will raise a KeyError. """

        def find_result_func(found_item, _):
            if found_item:
                return found_item[1:]
            else:
                raise KeyError(key)

        return self._find_by_key(key, find_result_func)

    def remove(self, key):
        """ Remove the object associated with key from the hashtable. If found, the object will
        be returned. If not found, KeyError will be raised. """

        def find_result_func(found_item, bucket):
            if found_item:
                bucket.remove(found_item)
                self._keys.remove(key)
                self.size -= 1
                return found_item[1]
            else:
                raise KeyError(key)
                

        return self._find_by_key(key, find_result_func)

    ####### Python's dict interface

    def keys(self):
        return self._keys

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.remove(key)

    def __repr__(self):
        return '{ ' + ', '.join([key + ':' + str(self.get(key)) for key in self._keys]) + ' }'

if __name__ == "__main__":
    # Run unit tests
    import unittest
    testsuite = unittest.TestLoader().discover('test', pattern="*hashtable*")
    unittest.TextTestRunner(verbosity=1).run(testsuite)




""" -------------------------- Queue (First in, first out) -------------------------- """

class SimpleQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)




""" -------------------------- Singly Linked List - O(1) Add/Delete, O(n) Search -------------------------- """

class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def show(self):
        node = self.head
        while node:
            if node.next != None:
                print node.data + " ->",
            else:
                print node.data
            node = node.next

    def get_head(self):
        return self.head






""" -------------------------- Stack (Last in, first out) -------------------------- """

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)