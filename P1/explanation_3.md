# Problem 3
## Abstract
I implemented huffman coding.
The description of huffman coding is below.
>A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

## Data structure
I used heap module for implementing binary tree based on frequency of characters.
Additionally I use dictionary for codes to character.

## Time analysis
Before modifying binary tree, we need to sort by frequency.
Thus, time order is O(NlogN) in the worst case for sorting where N is the length of frequency counted independent items.
After building up binary tree, huffman codes are with O(N) and encoding with O(N) because of one loop in there.
Finally, the decoding is O(N) with one loop for each character.
Totally this algorithm is O(NlogN)

## Space analysis
The space for binary tree is O(N) and dictionary of codes for character is O(N).
Totally it is O(N) for space.
