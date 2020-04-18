# Code Design
Here, two classes are present Block(which represents the block in block chain) and BlockChain (which itself represents BlockChain).

1. Block class contains instance variables and some method.
Instance Variables:
a. timestamp -
b. data
c. previous_hash - which contains the hash of previous block.
d. hash - contains the hash value of current block
e. next - which points the next block

Methods:
a. calc_hash: calculate hash of data of current node.
b. get_hash: returns the hash of the current block
c. get_utc_time: returns the timestamp

2. BlockChain class contains instance variables:
a. chain_dict: which contains the hash and block object as value.
b. head: points the head of the BlockChain
c. tail: points the tail of BlockChain
d. size: which keep tracks of size of BlockChain

Methods:
a. add_block: which sipmly add the block to BlockChain's tail and store the hash of previous block to its variable "previous_hash".
and increase the size of chain
b. print_blockchain: simply traverse the whole chain and print the values stored inside block
-------------------------------------------------------
# Time Complexity

add_block(): O(1)
print_blockchain(): O(n)

# Space Complexity

If, there are "n" blocks, then We need "n" nodes to our Block Chain and "n" elements to our chain dictionary.
So, it is O(n)
