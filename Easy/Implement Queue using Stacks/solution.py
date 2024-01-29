#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Implement Queue using Stacks' 
                problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "January 29, 2024"
class MyQueue:

    def __init__(self):
        # Queue implemented using 2 stacks, with stack operations only
        self.s1= []    # Used to insert and keep track of all elements
        self.s2 = []   # Used to return elements in a FIFO 

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        # Transfer all elements from stack1 to stack2
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append( self.s1.pop() ) 
         
        # Return the element in a FIFO queue mannar
        return self.s2.pop()

    def peek(self) -> int:
        # Transfer all elements from stack1 to stack2
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append( self.s1.pop() ) 
         
        # Return the element in a FIFO queue mannar
        return self.s2[ len(self.s2)-1]
        

    def empty(self) -> bool:
       return True if len(self.s1 + self.s2) == 0 else False

    # Custom function to return all elements of the queue in a list
    def checkElements(self) -> list:
        # Transfer all elements from stack1 to stack2
        while len(self.s1) != 0:
            self.s2.append( self.s1.pop() ) 
         
        # Return the element in a FIFO queue mannar
        return self.s2

def main():
    # Testing Class
    testQueue = MyQueue()

    # Insert data
    testQueue.push(1)
    testQueue.push(2)
    print("testQueue = {}".format(testQueue.checkElements()))

    # Return element at the front of the line
    frontElem = testQueue.peek()
    print("Element at the front of the line is {}".format(frontElem))

    # Remove the elemnet at the front of the line
    print("\nUsing pop() function,\nreturned {}".format(testQueue.pop()))
    print("\nAfter pop(),\ntestQueue = {}".format(testQueue.checkElements()))
    
    # Check if queue is empty
    print("\nIs testQueue empty?\n[Answer = {}]".format(testQueue.empty()))

main()