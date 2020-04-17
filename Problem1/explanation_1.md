# Code Design:
1. I used the combination of dictionary (for better lookup time) and doubly linked list for better insertion and deletion time.
2. My code consists of Instance variable (capacity lookup_dic) and methods( get, put) and a object of DoublyLinkedList

3. Let's talk about DoublyLinkedList class,
have instance variables:
a. head-  which points the starting Node
b. tail- points the last Node
c. no_of_ele- keeps tracks how many elements are in the cache
have methods:
a. update()- which updates the head node's value
b. insert()- insert node at the front of linkedlist
c. get_tail_key() - returns the key of last node of linkedlist
d. delete_tail() - delete the last Node
e. delete_middle() - delete the particular node

4. Now, it is good time to introduce the Put().
In the put function, I categorized it into some conditions,

Case 1. It may possible that the key we want to put is already present inside the lookup_dict and if it is not -1 so, it is the sign that I is still in our cache. Now, here came our sub-conditions and these are:
Case 1.1: Node with same key can be at head of the cache so, we simple change the value of head and our task is done.
Case 1.2: Node with same key can be at the tail of cache so, now make tail to tail's previous and we simply detach the tail. and insert at the front.
Case 1.3: Node can be somewhere in b/w the cache so, then simply detach the node from linkedlist and insert at the node in front with updated value.

Case 2. It is when the key is newly introducted to our lookup_dict so, simply insert it by calling DoublyLinkedList's insert() method

# Note:
Remember in all of this case, after insert node I inserted its, key along with link to inserted node to lookup_dict.
And after removing the any node I replaces its key's value inside the lookup_dict by -1.

5. Now talk about the get() function, there is two basic case either the value is present or not.
when value is not present in the cache it can be find by checking two conditions, either key is not in lookup_dict or value of lookup_dict[key]==-1
And When we can simply by the key and then we need to put it in the front.

# Complexity
Complexity of both operation is O(1)
