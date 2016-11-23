import random
with open('unsorted_ids.txt', 'w') as unsorted_ids:
    for i in range(100000):
        unsorted_ids.write(str(random.randint(0, 5000)))
        unsorted_ids.write("\n")
