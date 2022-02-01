from block import Block;

class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - Each block is a data set of transactions.
    """
    def __init__(self):
        self.chain = []
        # self.chain is going to contain a list of blocks

    # a way to add blocks to the blockchain:
    def add_block(self, data):
        self.chain.append(Block(data))
        # Creating an instance of class Block and appending it to blockchain.

    def __repr__(self):
        return f'Blockchain: {self.chain}'
        # repr method gives string representation rather than object at memory: <__main__.Blockchain object at 0x10f1fbb50>

def main():

    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)
    # Blockchain: [Block - data: one, Block - data: two]

    print(f'blockchain.py __name__: {__name__}')

if __name__ == '__main__':
    main()
