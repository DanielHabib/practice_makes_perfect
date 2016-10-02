
from enum import Enum
import json
from collections import defaultdict
print("Testing out a list as a default argument")
dictionary = defaultdict(list)
print(dictionary['hello'])
print(dictionary)

print("Testing out an initialized list as the default")
dictionary = defaultdict(lambda:[])
print(dictionary['bye'])
print(dictionary)


print("Testing out None Type, results in a key error")
adict = defaultdict(None)
#print(adict['foo'])
print(adict)

print("Testing a multilayered dictionary")
tree = lambda: defaultdict(tree)
adict = tree()
value = adict['Hello']['Govna']['Whatsup']['Bruh']
print(value)
print(value == {})
print(json.dumps(adict))


print("Trying to create an Enum with a class, is the enum really neccesary?")
class Name(Enum):
    foo = 1
print(Name.foo)
print(Name['foo'])
print(Name(1))
