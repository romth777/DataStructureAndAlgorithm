# Problem 6
## Abstract
I implemented union and intersection of two linked lists.
The description of union and intersection is below.
>The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

## Data structure
The given data structure is linked list.
In case of union I just connect two linked lists.
By the way, in case of intersection I used set module for duplicated linked list data, and then reconstruct linked list.

## Time analysis
In case of union the time order is O(N) for getting set of list1, O(M) for getting set of list2, and O(len(s) + len(t)) for unions by set modules where N is the size of linked list1, M is the size of linked list2, s is the set of linked list1 items, and t is the set of linked list2 items.
In case of intersection the time order is O(N) for getting set of list1, O(M) for getting set of list2, and O(min(len(s), len(t))) for intersections by set modules where N is the size of linked list1, M is the size of linked list2, s is the set of linked list1 items, and t is the set of linked list2 items.

## Space analysis
The space order is O(N+M) for each linked list.
