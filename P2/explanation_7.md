# Problem 7: Request Routing in a Web Server with a Trie
## Abstract
>For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

I solve this problem with Trie.

## Data structure
I used Tries to save path and send handler.

## Algorithm
To send handler I used recurrent function to get handler.

## Time analysis
Time complexity is O(N) where N is the max length of Tries.

## Space analysis
Space complexity is O(N) for Tries.
Additionally, my implementation is recurrent version of binary search so the function call stack needed O(logN).
