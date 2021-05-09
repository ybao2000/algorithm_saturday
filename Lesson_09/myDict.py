class myDict():   
  # all functions in class need self
  def __init__(self, size=1000): # constructor, __ means magic function, all these are just convention in python
    self._num = 0 # one _ means it's private
    self._size = size  # we don't want to expose this information to user, _ means internal use
    self.slots = [None] * self._size  # to store the keys
    self.data = [None] * self._size   # to store the values

  def put(self, key, value):
    if self._num  > self._size * 0.8:
      # you have to increase the size, and re-allot the keys and values
      pass
    index = self.hashfunction(key)
    if self.slots[index] is None: # empty slot
      self.slots[index] = key
      self.data[index] = value
      self._num += 1
    else:
      if self.slots[index] == key:  # same key, just change the value
        self.data[index] = value
      else:   # collision
        index2 = self.rehash(index)
        # continue rehash, until you either find am empty slot, or the slot has the same key
        while self.slots[index2] is not None and self.slots[index2] != key:
          index2 = self.rehash(index2)

        if self.slots[index2] is None:  # empty spot
          self.slots[index2] = key
          self.data[index2] = value
          self._num += 1          
        else:
          self.data[index2] = value

  def hashfunction(self, key):
    # # this is the place to map key to an index
    # # key could be anything
    # # int, bool, string, tuple, ...
    # if isinstance(key, int):
    #   return key % self._size
    # else:
    #   skey = str(key) # convert a key into a string
    #   sum = 0
    #   for c in skey:
    #     sum += ord(c)
    #   return sum % self._size
    return hash(key) % self._size

  def rehash(self, index):
    # linear probing
    return (index + 1) % self._size

  @property
  def num(self):
    return self._num

  def get(self, key):
    if self._num > 0:
      index = self.hashfunction(key)

      while self.slots[index] is not None:
        if self.slots[index] == key:  # you find it
          return self.data[index]
        else:
          index = self.rehash(index)
      else:
        return None
    else:
      return None

  def delete(self, key):
    if self._num > 0:
      index = self.hashfunction(key)
      while self.slots[index] is not None:
        if self.slots[index] == key:  # you find it
          value = self.data[index]
          self.slots[index] = None
          self.data[index] = None
          self._num -= 1
          return value
        else:
          index = self.rehash(index)
      else:
        return None
    else:
      return None

  # these 2 functions make it available []
  def __getitem__(self, key):
    return self.get(key)

  def __setitem__(self, key, value):
    self.put(key, value)

d = myDict(10000)
# d.put('apple', [1,2])
# d.put('banana', [2,3])
# print(d.Num())
# print(d.get('apple'))
# d.delete('apple')
# print(d.get('apple'))
d['apple'] = [1, 2]
d[3] = [3]
d['pear'] = [3, 4]
d['apple'] = [5, 6]
d[(1,2)] = '12'
print(d.num)
print(d[(1,2)])
