import hashlib
from time import gmtime, strftime


class BlockChain:
    def __init__(self):
        self.root = Block("Some Information", 0)
        self.current_node = self.root

    def add_block(self, data="Some Information"):
        new_block = Block(data, self.current_node.hash)

        if self.current_node == self.root:
            self.root.next_node = new_block

        self.current_node.next_node = new_block
        self.current_node = self.current_node.next_node


class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = self.get_timestamp()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.next_node = None

    def calc_hash(self, hash_str="We are going to encode this string of data!".encode('utf-8')):
        sha = hashlib.sha256()
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

    def get_timestamp(self):
        return strftime("%H:%M %m/%d/%Y", gmtime())


if __name__ == "__main__":
    blockchain = BlockChain()
    blockchain.add_block("I have a pen.")
    blockchain.add_block("I have an apple.")
    blockchain.add_block("Apple pen.")

    current_node = blockchain.root
    while current_node is not None:
        prev = current_node.previous_hash
        cur = current_node.hash
        assert prev != cur

        print('previous hash: {}'.format(current_node.previous_hash))
        print('data: {}'.format(current_node.data))
        print('current hash: {}'.format(current_node.hash))
        print('current timestamp: {}'.format(current_node.timestamp))
        print("-----")
        current_node = current_node.next_node


