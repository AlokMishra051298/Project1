# Code Design
Part 1: Huffman Coding
1. As we pass the data into huffman_encoding() then our first need to calculate the frequency of each character in present in our data.
So, we calculate frequency by call cal_char_freq() fuction.
After, getting the frequency we need to sort the frequencies into ascending order.
2. Now, I used a priority queue so, we can easily keep track of nodes (by frequency) in ascending order
3. We, build Priority Queue. The nodes of priority queue is like tree .i.e. each node have left and right variable.
4. Now, we need to build huffman tree, so we called build_huffman
5. When we got the tree, then we need to find the code by traversing the tree. So, we called the find_codes() which returns the dictionary with character as key along with their coded values.
6. Now, its time to encode our data, and now each character is replaced by the value in the dictionary returned by find_codes()
7. And at last, tree and encoded data is returned to main function

# Time Complexity
O(nlogn) - main time to insert "n" nodes into the Priority Queue (push- O(logn))

Part 2: Huffman Decoding
1. We start making decision by looking each bit of encoded data, if bit=0, then we need to move left of the present node and if bit=1 then we need to move right side.
2. Where we got the leaf node we add its char value to decode string and again start this process from head
3. We  continue this process until we traced each bit of encoded data.  
