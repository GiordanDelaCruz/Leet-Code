#!/usr/bin/env python
"""solution.py: This python file contains my solution to the 'Path Sum' problem on LeetCode.
                
                Note: A solution from with [USER] on [PLATFORM] helped me understand and solve the problem.   

                Link to video: [URL_LINK]
"""
__author__ = "Giordan Andrew"
__date__   = "February 25, 2025"
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        # Hitting Null 
        if root == None: 
            return False
        
        # Leaf node
        if root.left == None and root.right == None:
            # Check if path is equal our target sum
            return targetSum - root.val == 0
        
        targetSum -= root.val  # Parent node

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        

# ---------------------------------------------------------------------------------------------- #
# --------------                       NOT USEFUL START                               ---------- #
# ---------------------------------------------------------------------------------------------- #

    # InOrder: Root, LS, RS
    def inOrder(self, root):
        if root == None:
            return
        
        self.inOrder(root.left)
        print(root.val)
        self.inOrder(root.right)   

    # PreOrder: Root, LS, RS
    def preOrder(self, root):
        if root == None:
            return
        
        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

    
    # PostOrder: LS, RS, Root
    def postOrder(self, root):
        if root == None:
            return
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.val)

# ---------------------------------------------------------------------------------------------- #
# --------------                       NOT USEFUL END                                 ---------- #
# ---------------------------------------------------------------------------------------------- #



def main():
    solutionObj = Solution()

    # Test Data A
    node_a_l1_l2_l3 = TreeNode(7)
    node_a_r1_l2_r3 = TreeNode(2)
    node_a_r1_r2_r3 = TreeNode(1)
    node_a_l1_l2 = TreeNode(11, node_a_l1_l2_l3, node_a_r1_l2_r3)
    node_a_r1_l2 = TreeNode(13)
    node_a_r1_r2 = TreeNode(4, None, node_a_r1_r2_r3)
    node_a_l1 = TreeNode(4, node_a_l1_l2)
    node_a_r1 = TreeNode(8, node_a_r1_l2, node_a_r1_r2)
    root_a = TreeNode(5, node_a_l1, node_a_r1)
    target_sum_a = 22


    # Outputs
    output1 = solutionObj.hasPathSum(root_a, 22)

    # Display Results
    print("\n[Output1]: For Binary Tree with root = {}, finding a path_sum = {} is {}".format(root_a.val, target_sum_a, output1))

main()
