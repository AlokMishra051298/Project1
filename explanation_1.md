# Code Design:
1. I used the combination of dictionary (for better lookup time) and doubly linked list for better insertion and deletion time.
2. My code consists of Instance variable (capacity, current_len, head, tail, lookup_dic) and methods( get, put, insertFirst, show_cache).
3. Before talking about Put method I like to introduce my insertFirst() function which is here used to create node and place it at beginning of the cache.

Case 1. As we know before putting any key, value pair into cache our head of the cache is None so, in this case we simply create the node, make head and tail to the same node and increase the current length of cache.

Case 2. We can put the key, value pairs into cache upto the current_len==capacity so, before crossing this we need to put more data.
So, in that case, we simply create a node and insert it into the beginning of the cache. To do this, created node and current head have to point each other and then make created node to current head. And increase the current_len.

Case 3. Suppose the current_cache is full and we need to put the element in this case, we have to do two operations firstly, remove the last node and then insert the key, value pair we want to insert.

Note:
Remember in all of this case, after insert node I inserted its, key along with link to inserted node to lookup_dict.
And after removing the any node I replaces its key's value inside the lookup_dict by -1.

4. Now, it is good time to introduce the Put().
In the put function, I categorized it into some conditions,

Case 1. It may possible that the key we want to put is already present inside the lookup_dict and if it is not -1 so, it is the sign that I is still in our cache. Now, here came our sub-conditions and these are:
Case 1.1: Node with same key can be at head of the cache so, we simple change the value of head and our task is done.
Case 1.2: Node with same key can be at the tail of cache so, now make tail to tail's previous and we simply detach the tail. And now decrease the current_len of the cache because we removed the node and now call the insertFirst() function to put the passed key, value pair at head.
Case 1.3: Node can be somewhere in b/w the cache so, simply initialize the left and right to node's previous and next node and detach the node and again insert the node to the first by calling the insertFirst()

Case 2. It is when the key is newly introducted to our lookup_dict so, simply insert it by calling insertFirst()

5. Now talk about the get() function, there is two basic case either the value is present or not.
when value is not present in the cache it can be find by checking two conditions, either key is not in lookup_dict or value of lookup_dict[key]==-1
And When we can simply by the key and then we need to put it in the front.

# Complexity
Complexity of both operation is O(n)
   
