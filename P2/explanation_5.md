# Problem 5: Autocomplete with Tries
## Abstract
I solve this problem of suffix with recurrent function.

## Data structure
I used Tries to get suffix for lower space than saving any word.

## Algorithm
To get suffix I used recurrent function to get word from saved characters.

## Time analysis
Time complexity is O(N) where N is the max length of Tries.

## Space analysis
Space complexity is O(N) for Tries.
Additionally, my implementation is recurrent version of binary search so the function call stack needed O(logN).

