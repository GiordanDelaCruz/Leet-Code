#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Balanced Binary Tree' problem on LeetCode.
   Note: A solution from CheatCode Ninja helped me in understanding and solving this problem
         
   Link to Video: https://www.youtube.com/watch?v=dQp1oSkpyb4"""

__author__      = "Giordan Andrew"
__copyright__   = "December 20, 2022"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
   def isBalanced(self, root) -> bool:
        # Edge case
        if root == None:
            return True

        return checkSubTrees(root)[0]

def checkSubTrees(root):
    # Base Case
    if root == None:
        return True, 0
    
    leftSubTree = checkSubTrees(root.left)
    rightSubTree = checkSubTrees(root.right)
    rootHeight = max(leftSubTree[1], rightSubTree[1]) + 1
    diff = abs(rightSubTree[1] - leftSubTree[1])

    return leftSubTree[0] and rightSubTree[0] and diff <= 1, rootHeight
        

def main():
    # Binary Tree 1
    node_5 = TreeNode(5, None, None)
    node_4 = TreeNode(7, node_5, None)
    node_3 = TreeNode(15, None, None)
    node_2 = TreeNode(20, node_3, node_4)
    node_1 = TreeNode(9, None, None)
    root = TreeNode(3, node_1, node_2)

    # Binary Tree 2
    # node_1 = TreeNode(2, None, None)
    # root = TreeNode(1, None, node_1)

    # Binary Tree 3
    # node_6 = TreeNode(4, None, None)
    # node_5 = TreeNode(4, None, None)
    # node_4 = TreeNode(3, None, node_6)
    # node_3 = TreeNode(3, node_5, None)
    # node_2 = TreeNode(2, None, node_4)
    # node_1 = TreeNode(2, node_3, None)
    # root = TreeNode(1, node_1, node_2)

    solutionObj = Solution()
    output = solutionObj.isBalanced(root)
    print("The binary tree is {}".format(output))
main()