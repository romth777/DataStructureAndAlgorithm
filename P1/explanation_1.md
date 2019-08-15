# Problem 1
## Abstract
I implemented Least Recently Used (LRU) cache.
The description of LRU cache is below.
>An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. 

## Data structure
I used a dictionary module for implementing cache, the key of dictionary is given key and the value is list of the given value and counts of access for checking if to be removed when the chache reaches size limits.
In case of using dictionary the access order is O(1).

## Time analysis
Access time order is O(1) because of using dictionary and for frequency ranking it operates O(1) by ordered dictionary.
In my implementation the item which called move to the last of ordered dictionary.

## Space analysis
Space order is O(N) for dictionary and no need to allocate additional space where N is the size of cache.
