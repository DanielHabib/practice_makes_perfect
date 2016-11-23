from unittest import TestCase
import string
import random

class LLNode:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

    def addTail(self, key, value):
        if self.next:
            self.next.addTail(key, value)
        else:
            self.next = LLNode(key, value)
    
    def findNode(self, key):
        if key == self.key:
            return self
        if self.next:
            return self.next.findNode(key)

class Dictionary:
    """
        Things to Implement:
            Collision Handling
            Set and Get a Value, we shouldn't lose any values
            O(1) lookup


        Constraints:
            only support ASCII letter keys


    """
    def __init__(self ):
        self.keys = set()
        self.values = [None] * 100

    def __hash__(self, key):
        # Convert String into Key.
        index = 0
        totalSum = 0
        maxLength = 100
        counter = 1
        
        for letter in key:
            # Turn every character into a number
            totalSum += (ord(letter) * counter) # Ord is short for Ordinal
            counter += 1
        return totalSum % maxLength
   
    def __getitem__(self, key):
        return self.get_item(key)

    def __setitem__(self, key, value):
        self.set_item(key, value)

    def get_item(self, key):
        """Use Key to get the Value"""
        hashIndex = self.__hash__(key) 
        return self.values[hashIndex].findNode(key).value

    def set_item(self, key, value):
        """Use this to set the item """
            
        hashIndex = self.__hash__(key)

        if key in self.keys:
            Node = self.values[hashIndex]
            node = Node.findNode(key)
            node.value = value

        else:
            if self.values[hashIndex] is None: 
                self.values[hashIndex] = LLNode(key, value)
            else:
                self.values[hashIndex].addTail(key,value)
                

if __name__ == '__main__':
    dictionary = Dictionary()
    print(dictionary)


class DictionaryTest(TestCase):

    def test_can_get_set_item(self):
        key = "TestKey"
        value = "TestValue"
        dictionary = Dictionary()
        dictionary[key] = value
        self.assertEquals(value, dictionary[key])
    
    def test_can_get_set_multiple_values(self):
        key = "TestKey1"
        key2 = "TestKey2"
        value = "TestValue"
        value2 = "TestValue2"
        dictionary = Dictionary()
        dictionary[key] = value
        dictionary[key2] = value2
        self.assertEquals(value, dictionary[key])
        self.assertEquals(value2, dictionary[key2])

    def test_permutations(self):
        key = "TestKey"
        key2 = "KeyTest"
        value = "TestValue"
        value2 = "TestValue2"
        dictionary = Dictionary()
        dictionary[key] = value
        dictionary[key2] = value2
        self.assertEquals(value, dictionary[key])
        self.assertEquals(value2, dictionary[key2])

    def test_collision_handling(self):
        key = "c"
        key2 = "!!"
        value = "TestValue"
        value2 = "TestValue2"
        dictionary = Dictionary()
        dictionary[key] = value
        dictionary[key2] = value2
        self.assertEquals(value, dictionary[key])
        self.assertEquals(value2, dictionary[key2])

    def test_handle_robustness(self):
        dictionary = Dictionary()
        a_dict = {}
        for key in range(15215):
            
            key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
            value = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(25))

            a_dict[key] = value
            dictionary[key] = value

        for key in dictionary.keys:
            self.assertEquals(a_dict[key], dictionary[key])

    


