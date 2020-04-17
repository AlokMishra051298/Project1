import sys
#calculate the frequency of each letter
def cal_char_freq(string):
    freq_dict=dict()
    for key in string:
        if freq_dict.get(key):
            freq_dict[key]+=1
        else:
            freq_dict[key]=1
    return freq_dict
#Node
class Node:
    def __init__(self,frequency, char=None):
        self.char=char
        self.freq=frequency
        self.prev=None
        self.next=None
        self.left=None
        self.right=None

    def is_leaf(self):
        return (self.left is None and self.right is None)
#PriorityQueue implemented by doublly linked list node
class PriorityQueue:
    def __init__(self):
        self.head=None
        self.tail=None
    #add node to sure queue sorted order
    def add_node(self, node):
        if self.head is None:
            self.head=node
            self.tail=node
            return
        head=self.head
        while(head is not None and head.freq<=node.freq):
            head=head.next
        if head==self.head:
            node.next=self.head
            self.head.prev=node
            self.head=self.head.prev
            return
        #if we traverse through queue and need to insert node at tail
        if head==self.tail or head==None:
            self.tail.next=node
            node.prev=self.tail
            self.tail=self.tail.next
            return
        #node inserted in between the queue
        left=head.prev
        left.next=node
        head.prev=node
        node.prev=left
        node.next=head
        return
    #delete node from head
    def del_node(self):
        node=self.head
        self.head=self.head.next
        node.next=None
        node.prev=None
        return node
    # method to print queue
    def print_que(self):
        head=self.head
        while head is not None:
            print(head.char, head.freq)
            head=head.next
    # to check that queue is empty or not
    def is_empty(self):
        return self.head is None

#build Huffman tree .i.e. pick two nodes with lower frequency from Queue
#and build tree using that method
def build_huffman(queue):
    while(not queue.is_empty() and queue.head.next):
        node1=queue.del_node()
        node2=queue.del_node()
        sum_of_freq=node1.freq + node2.freq
        new_node=Node(sum_of_freq)
        new_node.left=node1
        new_node.right=node2
        queue.add_node(new_node)
    return queue

#this fuction helps to code every character by using the huffman tree
#returns the dictionay characteras key and code as value
def find_codes(tree):
    head=tree.head
    if head.is_leaf():
        return {tree.head.char:'0'}
    global code_list
    code_list=dict()
    codes(head, str())
    return code_list

def codes(head, string):
    arr=string
    #condition for left, if have left the add '0' to code string
    if head.left:
        string+='0'
        codes(head.left, string)
    #condition for right, if have right the add '1' to code string
    if head.right:
        string=arr
        string+='1'
        codes(head.right, string)
    # if we reached to leaf node then add the character along with their code to dictionary add
    if head.is_leaf():
        temp=string
        code_list[head.char]=temp
    return

#fuction huffman encoding to encode data
def huffman_encoding(data):
    #calculate the frequency of each character[ O(n) - "n" is no. of characters]
    char_freq=cal_char_freq(data)
    #sort the dictionary[O(klogk) - k is no. of items in dictionay, and if no. of items is equal to no. of characters in data then, O(nlogn)]
    sorted_freq=[(k, v) for k, v in sorted(char_freq.items(), key=lambda item: item[1])]
    queue=PriorityQueue()
    #add nodes with items in dictionay into PriorityQueue [O(n) in worst condition or in average O(k)]
    for item in sorted_freq:
        char=item[0]
        freq=item[1]
        node=Node(freq, char)
        queue.add_node(node)
    #this will build the huffman tree
    tree=build_huffman(queue)
    #helps to find out the codes from huffman tree
    get_code=find_codes(tree)
    #now encode data [O(n)]
    encoded_data=str()
    for x in data:
        encoded_data+=get_code[x]
    return encoded_data, tree


# huffman decoding function
def huffman_decoding(data,tree):
    data=str(data)
    head=tree.head
    string=str()
    #if we node is leaf the simply add the character to the decoded string
    if head.is_leaf():
        for x in data:
            string+=head.char
        return string
    #decode each character by tracing huffman tree
    for x in data:
        if head is not None:
            if x=="0":
                temp=head
                head=head.left
            elif x=="1":
                temp=head
                head=head.right
            #when we got leaf node the add char to decoded_data and
            #reinitialize the head and temp to root node of tree
            if head.is_leaf():
                string+=head.char
                head=tree.head
                temp=tree.head
    return string

if __name__ == "__main__":
#     codes = {}
    testcase=["Alok you can do it", "AAA", " ", "AAABBCCD", "ABCD"]
    count=1
    for case in testcase:
        print("Testcase {} ---------------".format(count))
        count+=1
        a_great_sentence = case

        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = huffman_encoding(a_great_sentence)
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))
