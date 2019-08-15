# Problem 4
## Abstract
I implemented whether if the user in group including sub grops.

## Data structure
I used list for pooling of groups.
First of all, pool the group of input and check if the group has users.
If the group has users, check if the target user is in the users.
Otherwise step into the next groups.

## Time analysis
The time order is O(logD) where D is the maximum depth of directories based on how many steps into groups recurrently.

## Space analysis
The space order is O(D) where D is the maximum depth of directories to pool groups for depth-wise. 
