import hashlib
from time import gmtime, strftime


class BlockChain:
    def __init__(self):
        self.root = None
        self.current_node = self.root
        self.num_nodes = 0

    def add_block(self, data):
        if data == "" or data is None:
            print("No input data!")
        else:

            if self.root is None:
                new_block = Block(data, 0)
                self.root = new_block
                self.current_node = self.root
            else:
                new_block = Block(data, self.current_node.hash)
                if self.current_node == self.root:
                    self.root.next_node = new_block

                self.current_node.next_node = new_block
                self.current_node = self.current_node.next_node
                self.num_nodes += 1

    def __str__(self):
        if self.root is None:
            return "Block chain empty!"
        else:
            return "{} blocks are in chain!".format(self.num_nodes)


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

    def __str__(self):
        ret = ""
        ret += 'previous hash: {}\n'.format(self.previous_hash)
        ret += 'data: {}\n'.format(self.data)
        ret += 'current hash: {}\n'.format(self.hash)
        ret += 'current timestamp: {}'.format(self.timestamp)
        return ret


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
        print(str(current_node))
        print("-----")
        current_node = current_node.next_node

    blockchain = BlockChain()
    print(blockchain)
    print("-----")

    blockchain = BlockChain()
    blockchain.add_block("")
    print("-----")

    blockchain = BlockChain()
    blockchain.add_block(None)
    print("-----")



