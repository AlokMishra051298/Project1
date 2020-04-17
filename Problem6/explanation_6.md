# Code Design
I don't know set is allowed or not. But as I read mentor's reply to someone's question, mentor mentioned that using built-in set functions we can't use.
So, I totally made my logic without using set.
I simply defined a function  remove_repetative(), this actually return new_lisked list without duplicates.
And in starting firstly remove all the duplicates which are present in both list.
Then,
In case of Union, firstly I add all the nodes of first linked list to union and then we trace union for each node in second linked list to check Is there any other node with same value, if node then append into the list or if there is duplicate the check for next node in second list.

In case of intersection we check for each node in llist1  to llist2 if there is node with same value the append to intersection.
I focused on corner cases too, like if both lists are empty, one of two is empty.

# Time complexity
let "n" elements in llist1 and "m" elements in llist2
then, time complexity for Union is O(n+m)
and time complexity for Intersection is O(n*m) 
