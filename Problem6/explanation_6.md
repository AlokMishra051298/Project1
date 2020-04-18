# Code Design
Mentor suggested that I can use set to optimize my code.
I firstly add elements of linked list 1 and 2 to set so, we can avoid duplicates and then used set operation to find out the union and intersection of both sets and the build linked list of result set using build_llist() function.

# Time complexity
let "n" elements in llist1 and "m" elements in llist2
then, time complexity for Union is O(n+m)
and time complexity for Intersection is O(n*m)
