# Code Design
We are looking at each level and the check into the groups and sub-groups and for each group we check that user is present in there users list or not.
And we repeat the process until we get the user. If after looking into group, if user is not present we returned False.

# Time Complexity
if we let, the given group have "n" users, then checking user in group's user list is O(n), if user is not present we have to look for the sub-groups let "k" sub-groups are there and here no. of calls depend on the depth of the structure, and for each call in worst case both conditional statements executes.
so, time complexity is O(depth*(n+k))

# Space complexity
User list= O(u)
group list=O(g)
for each iteration, O(u+g)
for n iteration, O(n*(u+g))
