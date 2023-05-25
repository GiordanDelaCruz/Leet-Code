#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Minimum Depth of Binary Tree' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "January 1, 2023"
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root):
        if root == None:
            return 0

        left_height = self.calculateHeight(root.left)
        right_height = self.calculateHeight(root.right)

        min_depth = min(left_height, right_height) + 1

        if left_height == 0:
            min_depth = right_height + 1
        elif right_height == 0:
            min_depth = left_height + 1

        return min_depth


    def calculateHeight(self, root):
        if root == None:
            return 0

        leftHeight = self.calculateHeight(root.left)
        rightHeiht = self.calculateHeight(root.right)

        return max(leftHeight, rightHeiht) + 1
        

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