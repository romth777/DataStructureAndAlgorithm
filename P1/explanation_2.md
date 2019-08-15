# Problem 2
## Abstract
I implemented Finding Files with given suffix from directories including sub directories.

## Data structure
I used recursive search algorithms, so I needed list for pooling next directory to search.

## Time analysis
Access time order is O(D) where D is the maximum depth of directories.
My recursive search iterates on the depth of recursion, thus time order is O(D).

## Space analysis
A space order is O(D) where D is the maximum depth of directories. 
My recursive search iterates on the depth of directories and in the worst case pool all the directories in the list.
Thus, the space needed O(D).
