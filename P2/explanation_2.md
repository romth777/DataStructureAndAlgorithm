# Problem 2: Search in a Rotated Sorted Array
## Abstract
Given a sorted array which is rotated at some random pivot point.
I solve this problem with binary search algorithm.

## Data structure
There is no need to use specific data structure in this task by using binary search.
However, an array is given.

## Algorithm
I used binary search algorithm for this task because the required time complexity is O(logN) where N is an target integer.
Binary search algorithm can search given sorted list with O(logN).
In this task given list is not sorted but rotated.
This means at least half of the given list is sorted, so my strategy is separate given list by half and if a half list is sorted, then look for the target is in there.
And then if there is no target number in the sorted list, make another half unsorted list half again, and continue.

## Time analysis
Required time complexity is O(logN) where N is size of array, and my implementation is on it.

## Space analysis
Space complexity is O(N) for given array.
Additionally, my implementation is recurrent version of binary search so the function call stack needed O(logN).
