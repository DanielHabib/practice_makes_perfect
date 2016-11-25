from unittest import TestCase
import string
import random


class Dictionary:
    """
        Things to Implement:
            Collision Handling
            Set and Get a Value, we shouldn't lose any values
            O(1) lookup


        Constraints:
            only support ASCII letter keys


    """
    
    def __init__(self, size=None):
        if size is None:
            size = 100
        self.values = [None] * size
        self.valueCount = 0
        self.randomSequence = list(range(size))
        self.currentProbeIteration = 0
        random.shuffle(self.randomSequence)
        self.arrayFull = False
        print(self.randomSequence)

    def hash_key(self, key):
        # We implemented the counter value to help remove collisions generated via permutations
        # Convert String into Key.
        index = 0
        totalSum = 0
        counter = 1
        
        for letter in key:
            # Turn every character into a number
            totalSum += (ord(letter) * counter) # Ord is short for Ordinal
            counter += 1
        return totalSum
    
    def generate_entry(self,hashValue, key, value):
        return "{hashValue}|{key}|{value}".format(hashValue=hashValue, key=key, value=value)

    def split_entry(self, entry):
        """
            @return in the format of [hashValue, key, value]
        """
        return entry.split("|")

    def __getitem__(self, key):
        return self.get_item(key)

    def __setitem__(self, key, value):
        self.set_item(key, value)

    def get_item(self, key):
        """Use Key to get the Value"""
        hashValue = self.hash_key(key)
        hashIndex = hashValue % len(self.values)
        return self.find_entry(hashIndex, hashValue, key)

    def find_entry(self, hashIndex, hashValue, key):
        entry = self.values[hashIndex]
        if entry is None:
            self.currentProbeIteration=0
            return None

        if entry == -1:
            hashIndex = self.probe(hashIndex, hashValue, key)
            return self.find_entry(hashIndex, hashValue, key)
        else:
            [chval, ckey, cval] = self.split_entry(entry)
            if chval == str(hashValue) and key == ckey:
                self.currentProbeIteration=0
                return cval

        hashIndex = self.probe(hashIndex, hashValue, key)
        return self.find_entry(hashIndex, hashValue, key)

    def grow(self):
        "It Grew"
        oldValues = [self.split_entry(entry) for entry in self.values if entry != None]

        self.__init__(len(self.values)*2)
        print(len(self.randomSequence))
        for valueSet in oldValues:
            self.set_item(valueSet[1], valueSet[2])
    def set_item(self, key, value):
        """Use this to set the item """
        hashValue = self.hash_key(key)
        hashIndex = hashValue % len(self.values)
        print(self.values)
        entry = self.generate_entry(hashValue, key, value)
        self.set_entry(hashIndex, hashValue, entry )
        self.currentProbeIteration=0
        self.valueCount += 1
        if self.arrayFull:
            self.grow()

    def set_entry(self, hashIndex, hashValue, entry):
        if self.values[hashIndex] is None or self.values[hashIndex] == -1:
            self.values[hashIndex] = entry
            
        else:
            hashIndex = self.probe(hashIndex, hashValue, entry)
            self.set_entry(hashIndex, hashValue, entry)
        
        
    def probe(self, hashIndex, hashValue, entry):
        # Linear Probing
        # return self.linear_probe(hashIndex)

        # Random Probing
        return self.random_probe(hashIndex)


    def linear_probe(self, hashIndex):
        return (hashIndex + 1) % len(self.values)
        
    def random_probe(self, hashIndex):
        print(len(self.randomSequence), self.currentProbeIteration)
        index = (hashIndex + self.randomSequence[self.currentProbeIteration]) % len(self.values)
        self.currentProbeIteration += 1
        if self.currentProbeIteration >= (len(self.values) // 2):
            self.arrayFull = True
        
        return index

if __name__ == '__main__':
    dictionary = Dictionary()
    print(dictionary)


class DictionaryTest(TestCase):

    def test_can_get_set_item(self):
        key = "TestKey"
        value = "TestValue"
        dictionary = Dictionary()
        dictionary[key] = value
        print(dictionary.values)
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

    def test_handle_100_values(self):
        dictionary = Dictionary()
        a_dict = {}
        for key in range(99):
            
            key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
            value = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(25))

            a_dict[key] = value
            dictionary[key] = value
        
        for key in a_dict.keys():
            self.assertEquals(a_dict[key], dictionary[key])

"""
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
"""
