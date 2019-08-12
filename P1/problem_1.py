from queue import Queue


class LRU_Cache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()

    def get(self, key):
        if key not in self.cache.keys():
            return -1
        else:
            self.cache[key][1] += 1
            return self.cache[key][0]

    def set(self, key, value):
        if len(self.cache) >= 5:
            min_freq = 10**9
            remove_key = 0
            for k, v in self.cache.items():
                if v[1] < min_freq:
                    remove_key = k
                    min_freq = v[1]
            self.cache.pop(remove_key)
        self.cache[key] = [value, 0]


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


