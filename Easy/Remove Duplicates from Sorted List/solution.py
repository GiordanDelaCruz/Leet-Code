#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Remove Duplicates from Sorted List' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Nov 30, 2022"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        curr_node = head
    
        while curr_node != None:

            # Skip duplicated node values
            while curr_node.next != None and curr_node.val == curr_node.next.val:
                curr_node.next = curr_node.next.next

            # Update current node
            curr_node = curr_node.next
            
        return head

def main():
    node_6 = ListNode(5, None)
    node_5 = ListNode(4, node_6)
    node_4 = ListNode(3, node_5)
    node_3 = ListNode(3, node_4)
    node_2 = ListNode(2, node_3)
    node_1 = ListNode(1, node_2)
    solutionObj = Solution()
    unique_list = solutionObj.deleteDuplicates(node_1)

    while unique_list != None:
        print(unique_list.val)
        unique_list = unique_list.next if unique_list else None

main()