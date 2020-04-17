class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

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
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
#This function will remove the repetative 'value' node from the linked list
def remove_repetative(llist):
    new_llist=LinkedList()
    temp=dict()
    head=llist.head
    while head is not None:
        if not temp.get(head.value):
            temp[head.value]=1
            new_llist.append(head.value)
        head=head.next
    return new_llist
#union function with no repetative values
def union(llist_1, llist_2):
    #if one of the two linked list is None, then remove its repetativevalues and return llist
    if llist_1.head is None and llist_2.head is None:
        return None
    if llist_1.head is None:
        llist_2=remove_repetative(llist_2)
        return llist_2
    if llist_2.head is None:
        llist_1=remove_repetative(llist_1)
        return llist_1
    #if none of two linkedlist is None, then firstly remove the repetative values from both list
    llist_1=remove_repetative(llist_1)
    llist_2=remove_repetative(llist_2)
    head1=llist_1.head
    head2=llist_2.head
    #make object of LinkedList
    union=LinkedList()
    #first append nodes of llist1 to union
    while head1 is not None:
        if union.head is None:
            union.append(head1.value)
        union_head=union.head
        while union_head is not None:
            #here we avoid adding duplicate nodes
            if union_head.value==head1.value:
                break
            union_head=union_head.next
        #if any node any node occur then then not at None so, we can't add the node
        if union_head is None:
            union.append(head1.value)
        head1=head1.next
    #adding nodes of llis_2 by avoiding addition of duplicate nodes to union
    while head2 is not None:
        union_head=union.head
        while union_head is not None:
            if union_head.value==head2.value:
                break
            union_head=union_head.next
        if union_head is None:
            union.append(head2.value)
        head2=head2.next
    return union

#this function return the intersection of two linked list is any of the list is none then, returns None
def intersection(llist_1, llist_2):
    if llist_1.head is None or llist_2.head is None:
        return None
    #removing the repetative nodes
    llist_1=remove_repetative(llist_1)
    llist_2=remove_repetative(llist_2)
    head1=llist_1.head
    #Linkedlist object
    intersection=LinkedList()
    #check for each node in llist_1 if it is it llist_2 then insert to intersection linkkedlist object
    while head1 is not None:
        head2=llist_2.head
        while head2 is not None:
            if head2.value==head1.value:
                intersection.append(head1.value)
            head2=head2.next
        head1=head1.next
    #if no value is in intersection then return None
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
