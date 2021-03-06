#used the doubly linked list so the put operation can be easy for us.
class Node:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
#LRU_cache class
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity=capacity #the capacity of the cache
        self.current_len=0 #keeps track of current_length of cache
        self.head=None # Points the head (first node) of cache
        self.tail=None #points to the tail(last node) of cache
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
            #if that node is at front the we only need to change its value and doesn't need any extra operation
            if node==self.head:
                self.head.value=value
                return
            #if that node is present at tail so, we only need to detach the last node and
            #shift the tail left side and insert that node in the front by using insertFirst() function
            elif node==self.tail:
                self.tail=self.tail.prev
                self.tail.next=None
                self.current_len-=1
                self.insertFirst(key,value)
                return
            #else the node is somewhere in cache except the head and tail, so we just remove it from the cache
            #and place it at head using insertFirst() function
            left=node.prev #previous node of the node which we want to remove
            right=node.next #next node of the node which we want to remove
            left.next=right #step to remove
            right.prev=left #step to remove
            self.current_len-=1 #decrease the current length of cache
            self.insertFirst(key, value) #and insert node at first
            return
        #if key is newly introduced to cache
        self.insertFirst(key, value)
        return

    def insertFirst(self, key, value):
        #if the cache is empty, insert the node into cache
        if self.head is None:
            node=Node(key, value)
            self.lookup_dict[key]=node
            self.head=node
            self.tail=node
            self.current_len+=1
            return
        #if the current length of cache is less the maximum capacity, then follow these steps
        if self.current_len+1<=self.capacity:
            node=Node(key, value)#create the node
            node.next=self.head #node points the head
            self.head.prev=node #now head.prev points to node
            self.head=node #make to node head
            self.lookup_dict[key]=node #and initialize that key, value pair into lookup_dict
            self.current_len+=1 #increase the current_len of cache
            return
        #If the cache is at capacity remove the oldest item.
        index=self.tail.key#index is the key which is now going to detach from cache
        self.lookup_dict[index]=-1 # set the value of removed index to -1 so, it is easy to keep track that no node is connected to it
        self.tail=self.tail.prev # shift tail to previous node
        self.tail.next=None #detach the tail
        self.current_len-=1 #decrease the current_length of cache
        self.insertFirst(key,value)#now simply add the key, value pair by calling the insertFirst() again
    def show_cache(self):
        head=self.head
        while head is not None:
            print(head.value)
            head=head.next

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
