# http://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/

import sys
import collections
from heapq import heappush, heappop


class Node:
    def __init__(self, value=None, char=None):
        self.value = value
        self.char = char
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, node):
        self.left = node

    def get_left_child(self):
        return self.left

    def has_left_child(self):
        return self.left is not None

    def set_right_child(self, node):
        self.right = node

    def get_right_child(self):
        return self.right

    def has_right_child(self):
        return self.right is not None

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        if self.left is None and self.right is None:
            return '{}:{} {} {}'.format(self.char, self.value, self.left, self.right)
        elif self.left is not None and self.right is None:
            return '{}:{} {}:{} {}'.format(self.char, self.value, self.left.char, self.left.value, self.right)
        elif self.left is None and self.right is not None:
            return '{}:{} {} {}:{}'.format(self.char, self.value, self.left, self.right.char, self.right.value)
        elif self.left is not None and self.right is not None:
            return '{}:{} {}:{} {}:{}'.format(self.char, self.value, self.left.char, self.left.value, self.right.char, self.right.value)


class HuffmanCoding:
    def __init__(self):
        self.char2code = dict()
        self.code2char = dict()

    def huffman_encoding(self, data):
        if data == "":
            return "No data to encode!", None
        splited_data = list(data)
        items = collections.Counter(splited_data).items()
        items = sorted(items, key=lambda x: x[1])
        h = []
        for item in items:
            n = Node(item[1], item[0])
            heappush(h, n)

        while len(h) != 1:
            z = Node()
            x = heappop(h)
            y = heappop(h)
            z.set_left_child(x)
            z.set_right_child(y)
            z.set_value(x.get_value() + y.get_value())
            heappush(h, z)
        hh = h.copy()

        root = heappop(h)
        current_code = ""
        if root.left is None and root.right is None:
            current_code = "0"

        def make_codes_helper(root, current_code):
            if root is None:
                return
            if root.char is not None:
                self.char2code[root.char] = current_code
                self.code2char[current_code] = root.char
                return
            make_codes_helper(root.left, current_code + "0")
            make_codes_helper(root.right, current_code + "1")

        make_codes_helper(root, current_code)

        encoded_data = []
        for item in splited_data:
            encoded_data.append(self.char2code[item])

        return ''.join(encoded_data), hh

    def huffman_decoding(self, data, tree):
        current_code = ""
        decoded_text = ""
        for bit in data:
            current_code += bit
            if current_code in self.code2char:
                character = self.code2char[current_code]
                decoded_text += character
                current_code = ""
        return decoded_text


if __name__ == "__main__":
    hc = HuffmanCoding()
    a_great_sentence = "The bird is the word"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = hc.huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = hc.huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    hc = HuffmanCoding()
    a_great_sentence = "AAAAAAAAAA"
    print("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = hc.huffman_encoding(a_great_sentence)
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = hc.huffman_decoding(encoded_data, tree)
    print("The content of the encoded data is: {}\n".format(decoded_data))

    hc = HuffmanCoding()
    a_great_sentence = ""
    print("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = hc.huffman_encoding(a_great_sentence)
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = hc.huffman_decoding(encoded_data, tree)
    print("The content of the encoded data is: {}\n".format(decoded_data))

