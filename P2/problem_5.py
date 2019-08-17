# Represents a single node in the Trie
class TrieNode:
    # Initialize this node in the Trie
    def __init__(self):
        self.is_word = False
        self.children = {}

    # Add a child node in this Trie
    def insert(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()

    # Recursive function that collects the suffix for
    # all complete words below this point
    def suffixes(self, suffix=''):
        words = list()

        def find_suffix(node, word):
            if node.is_word and word != "":
                words.append(word)

            for char in node.children:
                word += char
                find_suffix(node.children[char], word)

        find_suffix(self, "")

        return words


# The Trie itself containing the root node and insert/find functions
class Trie:
    # Initialize this Trie (add a root node)
    def __init__(self):
        self.root = TrieNode()

    # Add a word to the Trie
    def insert(self, word):
        current_node = self.root

        for char in word:
            current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    # Find the Trie node that represents this prefix
    def find(self, prefix):
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]

        return current_node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
f("ant")
