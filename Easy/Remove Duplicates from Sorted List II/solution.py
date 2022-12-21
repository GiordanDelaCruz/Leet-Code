#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Remove Duplicates from Sorted List II' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Dec 1, 2022"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        curr_node = head
        distinct_node = ListNode()
        distinct_node_head = distinct_node
        seen_nodes = []

        while curr_node:
            # Case 1: current node is a repeated element
            if curr_node.next != None and curr_node.val == curr_node.next.val:
                seen_nodes.append(curr_node.val)

                # Skip repeated elements
                while curr_node.next != None and curr_node.val != curr_node.next.val:
                    curr_node = curr_node.next

            # Case 2: current node is a distinct element
            elif curr_node != None and curr_node.val not in seen_nodes:
                new_node = ListNode(curr_node.val, None)
                distinct_node.next = new_node
                distinct_node = distinct_node.next
            curr_node = curr_node.next
        
        return distinct_node_head.next

def main():
    # Linked List 1 
    node_7 = ListNode(5, None)
    node_6 = ListNode(4, node_7)
    node_5 = ListNode(4, node_6)
    node_4 = ListNode(3, node_5)
    node_3 = ListNode(3, node_4)
    node_2 = ListNode(2, node_3)
    node_1 = ListNode(1, node_2)

    # Linked List 2
    # node_5 = ListNode(3, None)
    # node_4 = ListNode(2, node_5)
    # node_3 = ListNode(1, node_4)
    # node_2 = ListNode(1, node_3)
    # node_1 = ListNode(1, node_2)

    # Linked List 2
    # node_2 = ListNode(1, None)
    # node_1 = ListNode(1, node_2)

    # Linked List 3
    # node_3 = ListNode(2, None)
    # node_2 = ListNode(2, node_3)
    # node_1 = ListNode(1, node_2)

    solutionObj = Solution()
    distinct_list = solutionObj.deleteDuplicates(node_1)

    while distinct_list:
        print(distinct_list.val)
        distinct_list = distinct_list.next

main()