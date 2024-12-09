"""
    RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
"""
import random

class RandomizedSet(object):

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True


    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False
        # fetching val index
        val_index = self.dict[val]
        # replacing last element with val
        last_element = self.list[-1]
        self.list[val_index] = last_element
        # updating last element index with val index
        self.dict[last_element] = val_index
        # popping last element from list
        self.list.pop()
        # deleting val key from dict
        del self.dict[val]
        return True


    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list)

obj = RandomizedSet()

# inserting 2
val = 2
print(obj.insert(val))

# inserting 3
val = 3
print(obj.insert(val))

# again inserting 2
val = 2
print(obj.insert(val))

# removing 2
print(obj.remove(val))

# removing 5
val = 5
print(obj.remove(val))

# inserting 4
val = 4
print(obj.insert(val))

# fetching random element from list
print(obj.getRandom())