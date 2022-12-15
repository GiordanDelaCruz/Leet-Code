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
        
        # Edge case of array is empty
        if len(nums) == 0:
            return None

        # Convert array into a binary tree
        median = nums[len(nums)//2]
        root = TreeNode(median, None, None)

        # Create other nodes
        for idx, val in enumerate(nums):
            if val != root.val:
                print("node val in loop = {}".format(val))
                print("root val = {}".format(root.val))
                new_node = TreeNode(val, None, None)
                if val < root.val:
                    print("inserting into the left subtree")
                    insertNode(root, new_node, 'left')
                else:
                    print("inserting into the right subtree")
                    insertNode(root, new_node, 'right')
        return root

def insertNode(parent_node = None, child_node = None, direction = None):

    if direction == 'left':
        # DEBUG
        print("parent_node = {}".format(parent_node.val))
        if parent_node.left:
            print("left child_node = {}".format(parent_node.left.val))
        if parent_node.right:
            print("right child_node = {}".format(parent_node.right.val))
        # END OF DEBUG

        if parent_node and child_node.val < parent_node.val:
            if parent_node.left == None:
                print("inserting child_node = {} in the left node of {}\n".format(child_node.val, parent_node.val))
                parent_node.left = child_node
            else:
                print("Inside recursion call for left subtree")
                print("BEFORE - parent_node = {}".format(parent_node.val))
                parent_node = parent_node.left
                print("AFTER - parent_node = {}".format(parent_node.val))
                insertNode(parent_node, child_node, 'left')
            
        elif parent_node and child_node.val > parent_node.val:
            if parent_node.right == None:
                print("inserting child_node = {} in the right node of {}\n".format(child_node.val, parent_node.val))
                parent_node.right = child_node
            else:
                print("Inside recursion call for right subtree")
                print("BEFORE - parent_node = {}".format(parent_node.val))
                parent_node = parent_node.right
                print("AFTER - parent_node = {}".format(parent_node.val))
                insertNode(parent_node, child_node, 'right')


    elif direction == 'right':
        if parent_node and child_node.val > parent_node.val:
            if parent_node.right == None:
                print("inserting child_node = {} in the right node of {}\n".format(child_node.val, parent_node.val))
                parent_node.right = child_node
            else:
                print("Inside recursion call for right subtree")
                print("BEFORE - parent_node = {}".format(parent_node.val))
                parent_node = parent_node.right
                print("AFTER - parent_node = {}".format(parent_node.val))
                insertNode(parent_node, child_node, 'right')

        elif parent_node and child_node.val < parent_node.val:
            if parent_node.left == None:
                print("inserting child_node = {} in the left node of {}\n".format(child_node.val, parent_node.val))
                parent_node.left = child_node
            else:
                print("Inside recursion call for left subtree")
                print("BEFORE - parent_node = {}".format(parent_node.val))
                parent_node = parent_node.left
                print("AFTER - parent_node = {}".format(parent_node.val))
                insertNode(parent_node, child_node, 'left')

def inOrderTraversal(node): 
    if node == None:
        return None

    if node:
        inOrderTraversal(node.left)
        print("node val = {}".format(node.val))
        if node.left:
            print("child_left = {}".format(node.left.val))
        if node.right:
            print("child_right = {}".format(node.right.val))
        print("\n")
        inOrderTraversal(node.right)


def main():
    # Binary Tree 1
    node_4 = TreeNode(5, None, None)
    node_3 = TreeNode(-10, None, None)
    node_2 = TreeNode(9, node_4, None)
    node_1 = TreeNode(-3, node_3, None)
    root = TreeNode(0, node_1, node_2)

    solutionObj = Solution()
    input = [-10, -3, 0, 5, 9]
    output = solutionObj.sortedArrayToBST(input)
    # print("The output is {}".format(output))
    print("\n\n\n\n")
    inOrderTraversal(output)
    

main()