import copy
import random
import sys
random.seed(0)
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.current_node = None

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
            self.current_node = self.head
            return

        self.current_node.next = Node(value)
        self.current_node = self.current_node.next

    def concat(self, linked_list):
        self.current_node.next = linked_list.head
        self.current_node = linked_list.current_node

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    llist = copy.deepcopy(llist_1)
    llist.concat(llist_2)
    return llist


def intersection(llist_1, llist_2):
    # Your Solution Here
    set_1 = set()
    set_2 = set()

    node = llist_1.head
    while node.next:
        set_1.add(node.value)
        node = node.next

    node = llist_2.head
    while node.next:
        set_2.add(node.value)
        node = node.next

    items = set_1 & set_2

    llist = LinkedList()
    for item in items:
        llist.append(item)
    return llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [random.randint(0, 100) for i in range(10**2)]
element_2 = [random.randint(0, 100) for i in range(10**2)]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
print(intersection(linked_list_5, linked_list_6))