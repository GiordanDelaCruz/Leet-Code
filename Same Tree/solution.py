#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Same Tree' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Dec 3, 2022"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


      
def main():
    # Binary Tree 1 
    node_a2 = TreeNode(3, None, None)
    node_a1 = TreeNode(2, None, None)
    root_a = TreeNode(1, None, node_a1)

    # Binary Tree 2
    node_b2 = TreeNode(3, None, None)
    node_b1 = TreeNode(2, None, None)
    root_b = TreeNode(1, node_b1, node_b1)

    solutionObj = Solution()
    output = solutionObj.isSameTree(root_a, root_b)
    print("The answer is {}".format(output))

main()