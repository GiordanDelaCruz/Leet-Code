#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Symmetric Tree' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "December 10, 2022"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root) -> bool:
        # Edge case of empty Tree
        if root == None:
            return True
        
        return helper_check_symmetric(root.left, root.right)
        
def helper_check_symmetric(left_node, right_node):
    
    # Node with no children
    if left_node == None and right_node == None:
        return True
    # Node is not symmertical with its children
    elif left_node == None or right_node == None:
        return False
    
    # Check if the 2 children are equal
    if left_node.val != right_node.val:
        return False
    
    # Check nodes on lower levels
    return helper_check_symmetric(left_node.left, right_node.right) and helper_check_symmetric(left_node.right, right_node.left)

def main():
    # Binary Tree 1 
    node_l3 = TreeNode(3, None, None)
    node_l2 = TreeNode(4, None, None)
    node_l1 = TreeNode(2, node_l3, node_l2)
    node_r3 = TreeNode(3, None, None)
    node_r2 = TreeNode(4, None, None)
    node_r1 = TreeNode(2, node_r2, node_r3)
    root = TreeNode(1, node_l1, node_r1)

    solutionObj = Solution()
    output = solutionObj.isSymmetric(root)
    print("The solution is {}".format(output))

main()