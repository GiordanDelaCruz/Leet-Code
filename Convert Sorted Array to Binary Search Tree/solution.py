#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Convert Sorted Array to 
                Binary Search Tree' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "December 15, 2022"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        return createBalancedTree(nums)

def createBalancedTree(nums):

    # Edge case of array is empty
    if len(nums) == 0:
        return None

    # Convert array into a binary tree
    median_idx = len(nums)//2
    left_arr = nums[0:median_idx]
    right_arr = nums[median_idx+1:len(nums)]

    root = TreeNode(nums[median_idx], None, None)
    root.left = createBalancedTree(left_arr)
    root.right = createBalancedTree(right_arr)
    
    return root

def inOrderTraversal(root):
    if root == None:
        return None

    if root:
        inOrderTraversal(root.left)
        print(root.val)
        inOrderTraversal(root.right)

def main():
    # Binary Tree 1
    node_4 = TreeNode(5, None, None)
    node_3 = TreeNode(-10, None, None)
    node_2 = TreeNode(9, node_4, None)
    node_1 = TreeNode(-3, node_3, None)
    root = TreeNode(0, node_1, node_2)

    solutionObj = Solution()
    input = [-10, -3, 0, 5, 9]
    input = [0,1,2,3,4,5]
    output = solutionObj.sortedArrayToBST(input)
    # print("The output is {}".format(output.val))
    inOrderTraversal(output)
    

main()