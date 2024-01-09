#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Leaf-Similar Tree' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "January 9, 2024"
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
# Soltion to Leetcode Problem
class Soltuion:
    def leafSimilar(self, root1, root2):
        
        # Traverse through tree
        def DFS(root):
             # Edge case no root
            if not root: return []
          
            # Inorder traversal
            leaf_list = []
            if root:
                # Check if it is a leaf
                if root.left == None and root.right == None:
                    # Add node to leaf list
                    leaf_list += DFS(root.left)
                    leaf_list.append(root.val)
                    leaf_list += DFS(root.right)
            return leaf_list
        

        # Determine leaves
        leaf_list_a = DFS(root1)
        leaf_list_b = DFS(root2)

        # DEBUGGING
        print(leaf_list_a)
        print(leaf_list_b)

        # Check if there are equal number of leaves between both trees 
        if len(leaf_list_a) != len(leaf_list_b):
            return False

        # Check if sequence of leaves mathc between both trees
        for i in range(0, len(leaf_list_a)):
            if leaf_list_a[i] != leaf_list_b[i]:
                return False
        return True
    
def main():
    # [Test Data A]
    # Tree 1
    root_1a = TreeNode(3)
    root_1a.left = TreeNode(5)
    root_1a.right = TreeNode(1)
    root_1a.left.left = TreeNode(6)
    root_1a.left.right = TreeNode(2)
    root_1a.left.right.left = TreeNode(7)
    root_1a.left.right.right = TreeNode(4)
    root_1a.right.left = TreeNode(9)
    root_1a.right.right = TreeNode(8)
    # Tree 2
    root_1b = TreeNode(3)
    root_1b.left = TreeNode(5)
    root_1b.right = TreeNode(1)
    root_1b.left.left = TreeNode(6)
    root_1b.left.right = TreeNode(7)
    root_1b.right.left = TreeNode(4)
    root_1b.right.right = TreeNode(2)
    root_1b.right.right.left = TreeNode(9)
    root_1b.right.right.right = TreeNode(8)

    # [Test Data B]
    # Tree 1
    root_2a = TreeNode(1)
    root_2a.left = TreeNode(2)
    root_2a.right = TreeNode(3)
    # Tree 2
    root_2b = TreeNode(1)
    root_2b.left = TreeNode(3)
    root_2b.right = TreeNode(2)

    solutionObj = Soltuion()
    output_1 = solutionObj.leafSimilar(root_1a, root_1b)
    output_2 = solutionObj.leafSimilar(root_2a, root_2b)

    print("[Test Data A]: {}".format(output_1))
    print("[Test Data B]: {}".format(output_2))

main()