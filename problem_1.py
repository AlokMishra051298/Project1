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
    def update(self, head, value):
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
        self.cache=DoublyLinkedList() #object of DoublyLinkedList
        self.lookup_dict=dict() #used dictionary because of faster lookups

    def get(self, key):
        # The cases where the searched key is not present in the cache, so it returns -1
        if not self.lookup_dict.get(key) or self.lookup_dict[key]==-1:
            return -1
        #Get the value corresponding to key and put this node on the first position
        value=self.lookup_dict[key].value
        self.put(key,value)
        return value

    def put(self, key, value):
    # if the key appeared before and present in the cache
        if self.lookup_dict.get(key) and self.lookup_dict[key]!=-1:
            node=self.lookup_dict[key]
            #if that node is at front the we only need to update its value and doesn't need any extra operation
            if node==self.cache.head:
                self.cache.update(value)
                return
            #if that node is present at tail so,
            # we only need to detach the last node and
            # shift the tail left side and insert
            # that node in the front by using insert() of DoublyLinkedList
            elif node==(self.cache.tail):
                self.cache.delete_tail()
                self.lookup_dict[key]=self.cache.insert(key,value)
                return
            #else the node is somewhere in cache except the head and tail, so we just remove it from the cache
            #and place it at head using insert() of the DoublyLinkedList class.
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

#-------------------------------------------------------------------------
#Test cases are here
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

# Corner cases 1.
#What if the node is already occured once but didn't present in the LRU_cache
#and now we need to add it
our_cache.put(3,3)
