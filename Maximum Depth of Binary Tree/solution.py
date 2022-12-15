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
    def maxDepth(self, root):
        if root == None:
          return 0

        leftHeight = 0
        rightHeight = 0

        leftHeight += self.maxDepth(root.left)
        rightHeight += self.maxDepth(root.right)
        return max(leftHeight, rightHeight) + 1
        
def main():
    # Binary Tree 1
    node_4 = TreeNode(7, None, None)
    node_3 = TreeNode(15, None, None)
    node_2 = TreeNode(20, node_3, node_4) 
    node_1 = TreeNode(9, None,  None)
    root = TreeNode(3, node_1, node_2)

    solutionObj = Solution()
    output = solutionObj.maxDepth(root)
    print("The maximim depth of the tree is {}".format(output))

main()