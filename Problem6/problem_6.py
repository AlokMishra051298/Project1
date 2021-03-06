class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            self.tail=self.head
            return
        self.tail.next=Node(value)
        self.tail=self.tail.next

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def build_llist(llset):
    new_llist=LinkedList()
    for x in llset:
        new_llist.append(x)
    return new_llist


def return_set(llist):
    llset=set()
    head = llist.head
    while head is not None:
        llset.add(head.value)
        head=head.next
    return llset

def union(llist_1, llist_2):
    #if one of the two linked list is None, then remove its repetativevalues and return llist
    if llist_1.head is None and llist_2.head is None:
        return None
    if llist_1.head is None:
        set1=return_set(llist_2)
        llist_2=build_llist(set1)
        return llist_2
    if llist_2.head is None:
        set1=return_set(llist_1)
        llist_1=build_llist(set1)
        return llist_1

    set1=return_set(llist_1)
    set2=return_set(llist_2)
    result_set=set1.union(set2)
    #make object of LinkedList
    union=build_llist(result_set)
    return union

#this function return the intersection of two linked list is any of the list is none then, returns None
def intersection(llist_1, llist_2):
    if llist_1.head is None or llist_2.head is None:
        return None
    set1=return_set(llist_1)
    set2=return_set(llist_2)
    result_set=set1.intersection(set2)
    #make object of LinkedList
    intersection=build_llist(result_set)
    if intersection.head is None:
        return None
    return intersection

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
print("Testcase 1")
print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
print("----------------------")
# Test case 2
print("Testcase 2")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
print("----------------------------------")
#Testcase 3
print("Testcase 3")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
element_5=[]
element_6=[5,4]
for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))
print("----------------------------------")
