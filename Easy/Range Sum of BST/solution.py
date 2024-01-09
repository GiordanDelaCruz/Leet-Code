#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Range Sum of BST' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "January 9, 2024"
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Soltion to Leetcode Problem
class Solution:
        
    def rangeSumOfBST(self, root, low, high):
        def DFS(root):

            if root == None:
                return 0
            
            # Traverse through tree
            if root:
                # Add value to sum if its in the range
                if root.val >= low and root.val <= high:
                    return root.val + DFS(root.left) + DFS(root.right)
                else:
                    return 0 + DFS(root.left) + DFS(root.right)
                
        return DFS(root)
    
def main():
    # Test Data A
    root_a = TreeNode(10, 5, 15)
    root_a.left = TreeNode(5, 3, 7)
    root_a.right = TreeNode(15, None, 18)
    root_a.left.left = TreeNode(3, None, None)
    root_a.left.right = TreeNode(7, None, None)
    root_a.right.right = TreeNode(18, None, None)
    low_a = 7
    high_a = 15

    solutionObj = Solution()
    output_a = solutionObj.rangeSumOfBST(root_a, low_a, high_a)

    print("[Test Data A]: The range sum is {}".format(output_a))

main()