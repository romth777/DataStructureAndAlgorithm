from collections import OrderedDict


class LRU_Cache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if self.capacity <= 0:
            return -1
        if key not in self.cache.keys():
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def set(self, key, value):
        if self.capacity <= 0:
            print("Can't perform operations on 0 capacity cache")
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value


if __name__ == "__main__":
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    assert our_cache.get(1) == 1       # returns 1
    assert our_cache.get(2) == 2       # returns 2
    assert our_cache.get(9) == -1      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    assert our_cache.get(3) == -1      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print(our_cache.cache)

    our_cache = LRU_Cache(2)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(1, 10)
    assert our_cache.get(1) == 10
    assert our_cache.get(2) == 2

    our_cache = LRU_Cache(0)
    our_cache.set(1, 1)
    assert our_cache.get(1) == -1


