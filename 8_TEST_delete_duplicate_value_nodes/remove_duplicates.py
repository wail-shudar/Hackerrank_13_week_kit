#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)



#
# Complete the 'removeDuplicates' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeDuplicates(llist):
    detected = False
    head = temp = llist
    
    while llist:        
        if llist.next:
            if not detected and llist.data == llist.next.data:
                temp = llist
                detected = True
            elif detected and llist.data != llist.next.data: 
                temp.next = llist.next
                detected = False
        elif detected: temp.next = None
        llist = llist.next
    return head
    
# recursive alt. solution by: https://www.hackerrank.com/profile/mwilli20
# def RemoveDuplicates(head):
#     if head == None:
#         return None
#     elif head.next == None:
#         return head
#     elif head.data == head.next.data:
#         return RemoveDuplicates(head.next)
#     else: 
#         return Node(head.data, RemoveDuplicates(head.next))

def removeDuplicates(llist):
    detected = False
    while llist:
        temp = 0
        if not detected and list.data == llist.next.data:
            temp = llist
            detected = True
        elif detected and list.data != llist.next.data: 
            temp.next = llist
            detected = False
        llist = llist.next


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        llist_count = int(input().strip())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input().strip())
            llist.insert_node(llist_item)

        llist1 = removeDuplicates(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
