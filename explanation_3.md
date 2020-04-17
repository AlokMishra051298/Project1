# Code design
The function simply the path if it is with suffix then, append into the list else check Is it directory if yes, then repeat this process for each sub directories and if path is neither satisfies any of  upper two conditions then return the existing list.

# Complexity
The complexity depend on the depth and breadth of the directory:
let if directory have "n" subdirectories and each sub directory have "f" no. of files.
Then we have to go through each directory once and have to check each file
so, the complexity in that case

**O(n*f)**
