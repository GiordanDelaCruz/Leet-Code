#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Adding Two Numbers' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Nov 21, 2022"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:

        dummy_head = ListNode(0) # Create a new linked list to hold the sum
        curr_node = dummy_head
        carry = 0
      
        while l1 != None or l2 != None or carry != 0:
            l1_val = l1.val if l1 != None else 0
            l2_val = l2.val if l2 != None else 0
            col_sum = l1_val + l2_val + carry
            carry = sum // 10 # Floor division in Python
            new_node = ListNode(col_sum%10) # Save col_sum in final sum solution
            curr_node.next = new_node # Connect final sum nodes
            curr_node = new_node
            l1 = l1.next if l1 else None #[Note: Not sure what this does yet]
            l2 = l2.next if l2 else None

        return dummy_head.next

#----------------------------------------------------------------------------------------------------
#------------------                   TESTING & DEBUGGING                               -------------
#----------------------------------------------------------------------------------------------------
def main():
    soultionObj = Solution()
    node_a1 = ListNode(2, 4)
    node_a2 = ListNode(4, 3)
    node_a3 = ListNode(3)

    node_b1 = ListNode(5, 6)
    node_b2 = ListNode(6, 4)
    node_b3 = ListNode(4)

    # linked_list_1 = [node_a1, node_a2, node_a3]
    # linked_list_2 = [node_b1, node_b2, node_b3]
    # sum = soultionObj.addTwoNumbers(linked_list_1, linked_list_2)

    sum = soultionObj.addTwoNumbers(node_a1, node_b2)
    print("The sum is {}".format(sum))
    
    # Linked List 1
    # for i in range(0, len(linked_list_1)):
    #     print(linked_list_1[i].val, end='')
    # print('\n')

    # Linked List 2
    # for i in range(0, len(linked_list_2)):
    #     print(linked_list_2[i].val, end='')

main()
