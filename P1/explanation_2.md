# Problem 2
## Abstract
I implemented Finding Files with given suffix from directories including sub directories.

## Data structure
I used recursive search algorithms, so I use list for pooling next directory to search.
Especially this is like a DFS using list as a stack.

## Time analysis
Access time order is O(D) where D is the maximum depth of directories.
In my DFS like searching I did not implementing pruning, so my algorithm needs to access all of the files.

## Space analysis
In the recursive function we need more space than non-recursive functions.
A space order is O(D) where D is the maximum depth of directories. 
