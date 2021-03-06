#used the doubly linked list so the put operation can be easy for us.
class Node:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
#doublylinkedlist class I defined only those methods which are needed for LRU_Cache
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.no_of_ele=0

    def insert(self, key, value):
        if self.head is None:
            node=Node(key, value)
            self.head=node
            self.tail=node
            self.no_of_ele+=1
            return self.head
        node=Node(key, value)#create the node
        node.next=self.head #node points the head
        self.head.prev=node #now head.prev points to node
        self.head=node #make to node head
        self.no_of_ele+=1
        return self.head

    #update the value of head node
    def update(self, value):
        self.head.value=value

    def get_tail_key(self):
        return self.tail.key

    def delete_tail(self):
        self.tail=self.tail.prev
        self.tail.next=None
        self.no_of_ele-=1

    '''This method helps to remove the node which is present
    in head and tail'''
    def delete_middle(self, node):
        ptr=self.head
        while(ptr!=node):
            ptr=ptr.next
        left_ptr=ptr.prev
        right_ptr=ptr.next
        left_ptr.next=right_ptr
        right_ptr.prev=left_ptr
        self.no_of_ele-=1
#--------------------------------------------------------------------------
class LRU_Cache:

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity=capacity #the capacity of the cache
        self.cache=DoublyLinkedList()
        self.lookup_dict=dict() #used dictionary because of faster lookups

    def get(self, key):
        # if self.capacity==0:
        #     return "You can't access anything from queue because Capacity of queue is Zero(0)"
        # The cases where the searched key is not present in the cache, so it returns -1
        if not self.lookup_dict.get(key) or self.lookup_dict[key]==-1:
            return -1
        #Get the value corresponding to key and put this node on the first position
        value=self.lookup_dict[key].value
        self.put(key,value)
        return value

    def put(self, key, value):
        #edge case if capacity is empty
        if self.capacity==0:
            return "You can't add anything to queue because Capacity of queue is Zero(0)"
        # if the key appeared before and present in the cache
        if self.lookup_dict.get(key) and self.lookup_dict[key]!=-1:
            node=self.lookup_dict[key]
            #if that node is at front the we only need to change its value and doesn't need any extra operation
            if node==self.cache.head:
                self.cache.update(value)
                return
            #if that node is present at tail so, we only need to detach the last node and
            #shift the tail left side and insert that node in the front by using insert() function
            elif node==self.cache.tail:
                self.cache.delete_tail()
                self.lookup_dict[key]=self.cache.insert(key,value)
                return
            #else the node is somewhere in cache except the head and tail, so we just remove it from the cache
            #and place it at head using insertFirst() function
            self.cache.delete_middle(node)
            self.lookup_dict[key]=self.cache.insert(key,value) #and insert node at first
            return
        #if key is newly introduced to cache

        #if the current length of cache is less the maximum capacity, then follow these steps
        if self.cache.no_of_ele+1<=self.capacity:
            node=self.cache.insert(key, value)
            self.lookup_dict[key]=node #and initialize that key, value pair into lookup_dict
            return
        #If the cache is at capacity remove the oldest item.
        index=self.cache.get_tail_key()#index is the key which is now going to detach from cache
        self.lookup_dict[index]=-1 # set the value of removed index to -1 so, it is easy to keep track that no node is connected to it
        self.cache.delete_tail() #detach the tail
        #now simply add the key, value pair by calling insert()
        self.lookup_dict[key]=self.cache.insert(key, value)
        return

our_cache = LRU_Cache(5)

our_cache.put(1, 1);
our_cache.put(2, 2);
our_cache.put(3, 3);
our_cache.put(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.put(5, 5)
our_cache.put(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
#-------------------------------------------------------------------------
#Test case1
our_cache = LRU_Cache(5)

our_cache.put(1, 1);
our_cache.put(2, 2);
our_cache.put(3, 3);
our_cache.put(4, 4);

print("_________TEST CASE 1_________________")
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.put(5, 5)
our_cache.put(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Corner cases 1.
#What if the node is already occured once but didn't present in the LRU_cache
#and now we need to add it
our_cache.put(3,3)

#--------------------------------------------------
#Test case 2
print("_________TEST CASE 2_________________")
new_cache = LRU_Cache(3)
new_cache.put(1, "A")
new_cache.put(2, "L")
new_cache.put(3, "O")
new_cache.put(4, "K")

print(new_cache.get(2))
print(new_cache.get("O"))
new_cache.put(5, "M")
print(new_cache.get(1))
print(new_cache.get(4))
print(new_cache.get(2))
#----------------------------------------------------------
#testcase 3
print("_________TEST CASE 3_________________")
fee_queue=LRU_Cache(4)
fee_queue.put(1,"ALOK")
fee_queue.put(2,"AMAN")
fee_queue.put(1,"ANJALI")
print(fee_queue.get(1))
fee_queue.put(3,"ABHISHEK")
fee_queue.put(4,"ANKITA")
fee_queue.put(5,"RASHMI")
print(fee_queue.get(2))

print("_________EDGE CASE _________________")
zero_capacity=LRU_Cache(0)
print(zero_capacity.get(0))
