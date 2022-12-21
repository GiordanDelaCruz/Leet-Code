#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Binary Tree Inorder Traversal' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Dec 3, 2022"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        # Edge case no root
        if not root: return []

        node_vals = []
        if root: 
            print(root.val)
            node_vals += self.inorderTraversal(root.left)
            node_vals.append(root.val)
            node_vals += self.inorderTraversal(root.right)
        return node_vals

      
def main():
    # Binary Tree # 1 
    node_2 = TreeNode(3, None, None)
    node_1 = TreeNode(2, node_2, None)
    root = TreeNode(1, None, node_1)

    solutionObj = Solution()
    output = solutionObj.inorderTraversal(root)
    print("The output of nodes are {}".format(output))

main()