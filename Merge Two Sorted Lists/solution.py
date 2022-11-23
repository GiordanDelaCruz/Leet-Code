#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Merge Two Sorted Lists' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Nov 23, 2022"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        dummy_head = ListNode(0)
        merged_list = dummy_head

        # Compare values inside nodes
        while list1 != None or list2 != None:
            # DEBUG
            # print('List 1: {}'.format(list1.val)) if list1 != None else print("List 1: Empty")
            # print('List 2: {}\n'.format(list2.val)) if list2 != None else print("List 2: Empty")

            # Check if list1 or list2 is no empty 
            if list1 != None and list2 != None:
                if list1.val <= list2.val:
                    new_node = ListNode(list1.val)
                    list1 = list1.next
                else:
                    new_node = ListNode(list2.val)
                    list2 = list2.next
            else:
                if list1 == None:
                    new_node = ListNode(list2.val)
                    list2 = list2.next
                else:
                    new_node = ListNode(list1.val)
                    list1 = list1.next

            merged_list.next = new_node
            merged_list = new_node

        return dummy_head.next
          
def main():
    solutionObj = Solution()
    # Linked List 1
    node_a3 = ListNode(4)
    node_a2 = ListNode(2, node_a3)
    node_a1 = ListNode(1, node_a2)
    # Linked List 2
    node_b3 = ListNode(4)
    node_b2 = ListNode(3, node_b3)
    node_b1 = ListNode(1, node_b2)

    linked_list_merged = solutionObj.mergeTwoLists(node_a1, node_b1)
    
    # Print output
    while linked_list_merged != None:
        print(linked_list_merged.val, end=' ')
        linked_list_merged = linked_list_merged.next if linked_list_merged else None

main()