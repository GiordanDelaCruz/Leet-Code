#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Balanced Binary Tree' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "December 15, 2022"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root) -> bool:
        
            if root == None:
                return True

            if root.left == None and root.right == None:
                return True

            if root:
                left_sub_tree_height = self.determineHeight(root.left) if root.left else 0
                right_sub_tree_height = self.determineHeight(root.right) if root.right else 0
                
                print("The left subtree height = {}".format(left_sub_tree_height))
                print("The right subtree height = {}".format(right_sub_tree_height))

                diff = right_sub_tree_height - left_sub_tree_height
                print("diff = {}".format(diff))
                if diff >= -1 and diff <= 1:
                    return True
                else:
                    return False
            
    def determineHeight(self, root):
        # Base case
        if root == None:
            return 0
    
        left_height = 0 
        right_height = 0

        left_height += self.determineHeight(root.left)
        right_height += self.determineHeight(root.right)
        
        print("The left_height = {}".format(left_height))
        print("The right_height = {}".format(right_height))
        return max(left_height, right_height) + 1

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
    # Binary Tree 1
    node_5 = TreeNode(5, None, None)
    node_4 = TreeNode(7, node_5, None)
    node_3 = TreeNode(15, None, None)
    node_2 = TreeNode(20, node_3, node_4)
    node_1 = TreeNode(9, None, None)
    root = TreeNode(3, node_1, node_2)

    # Binary Tree 2
    node_1 = TreeNode(2, None, None)
    root = TreeNode(1, None, node_1)

    # Binary Tree 3
    node_6 = TreeNode(4, None, None)
    node_5 = TreeNode(4, None, None)
    node_4 = TreeNode(3, None, node_6)
    node_3 = TreeNode(3, node_5, None)
    node_2 = TreeNode(2, None, node_4)
    node_1 = TreeNode(2, node_3, None)
    root = TreeNode(1, node_1, node_2)

    solutionObj = Solution()
    output = solutionObj.isBalanced(root)
    print("The binary tree is {}".format(output))
    
    print("\n\nInorder Travaersal:\n")
    node_list = solutionObj.inorderTraversal(root)
    print(node_list)
main()