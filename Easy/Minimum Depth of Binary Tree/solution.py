#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Minimum Depth of Binary Tree' problem on LeetCode.
  
                Note: A solution from GeeksForGeeks helped me understand and solve the problem. My code utilizies
                      a Depth First Search (DFS) approach, which means I calcalaute the Depth of each left and right
                      subtress.

                Link to website: https://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/
"""
__author__      = "Giordan Andrew"
__date__   = "February 25, 2025"
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root):
        # Edge Case: Only Root
        if root == None:
            return 0

        # Check if Node is a leaf
        if root.left == None and root.right == None:
            return 1
        
        # Recur and calculate remaining heights for Left and Right Subtress
        if root.left == None:
            # Implies that this is a parent node, with right child. 
            # (We know it cannot be a leaf from previous if-statement)
            return self.minDepth(root.right) + 1  # Add 1 due to the parent
            
        if root.right == None:
            # Implies that his is a parent node with a left child. 
            # (We know it cannot be a lead from the previous if-statement)
            return self.minDepth(root.left) + 1   # Add 1 due to the parent
           
        min_depth = min( self.minDepth(root.left), self.minDepth(root.right) ) + 1  # Add one due to the parent
        return min_depth


def main():
    node_4 = TreeNode(7, None, None)
    node_3 = TreeNode(15, None, None) 
    node_2 = TreeNode(20, node_3, node_4)
    node_1 = TreeNode(9, None, None)
    root = TreeNode(3, node_1, node_2)
    solutionObj = Solution()
    output = solutionObj.minDepth(root)
    print("The Minimum depth of the binary tree is {}".format(output))

    

main()