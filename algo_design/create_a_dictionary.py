import string
from functools import lru_cache
'''
ADT Dictionary:
    Search : O(1)
    Insert : O(1)
    Delete : O(1)

Collisions Handled Via Chaining
    All Values need to be unique
    All keys must be lower case strings
'''


class LinkedListNode:
    def __init__(self, key, value, next=None):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})

    def __repr__(self):
        return 'Linked List Node With Value:{}'.format(self.value)

    def findNodeWithKey(self, key):
        if self.key == key:
            return self.value
        if self.next is None:
            return None
        return self.next.findNodeWithKey(key)

    def addTail(self,key, value):
        ''' '''
        if self.next is None:
            self.next = LinkedListNode(key,value)
        else:
            self.next.addTail(value)

    def deleteNextNodeWithValue(self, value):
        if not node.next:
            raise Exception('Value NOt Found')
        if node.next.value == value:
            node.next = node.next.next
        else:
            node.next.deleteNextNodeWithValue(value)


class Dictionary:
    def __init__(self, arrLength=100):
        self.arrLength = arrLength
        self.arr = [None] * self.arrLength


    @lru_cache(maxsize = 100)
    def _hash(self, x):
        '''Turns a string into a Hash'''
        alphabet = string.ascii_lowercase
        score = 0
        for letter in x:
            score += alphabet.index(letter) + 1
        print('Hash Value for {0}, is equal to {1}'.format(x, score % self.arrLength))
        return score % self.arrLength

    def insert(self, key, value):
        '''Insert'''
        hvalue = self._hash(key)
        if self.arr[hvalue] is None:
            self.arr[hvalue] = LinkedListNode(key, value)
        else:
            self.arr[hvalue].addTail(key, value)

    def delete(self, x):
        '''Delete'''
        hvalue = self._hash(x)
        if self.arr[hvalue] is None:
            raise Exception('Value Doesnt Exist')
        if self.arr[hvalue].next is None:
            self.arr[hvalue] = None
        else:
            self.arr[hvalue].deleteNodeWithValue(x)

    def search(self, x):
        '''Search'''
        hvalue = self._hash(x)
        if self.arr[hvalue] is None:
            return None
        return self.arr[hvalue].findNodeWithKey(x)


if __name__ == '__main__':
    a_dict = Dictionary()
    a_dict.insert('foo', 10)
    print(a_dict.search('foo'))
    a_dict.insert('bar', 20)
    print(a_dict.search('bar'))
    a_dict.insert('varchar', 'hello')
    print(a_dict.search('varchar'))
    a_dict.insert('arb', 60)
    print(a_dict.search('arb')) # Note the LRU Cache(Least Recenetly Used)
                                # Allows us to save some function calls
                                # to the _hash method
    print(a_dict.search('bar'))
