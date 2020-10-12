"""
Implement a stack that accepts the following commands and performs the operations described:

push v: Push integer v onto the top of the stack
pop: Pop the top element from the stack
inc i v: Add v to each of the bottom i elements of the stack

After each operation, print the value at the top of the stack. If the stack is empty, print the string 'EMPTY'

Example:
operations = ['push 4', 'push 5', 'inc 2 1', 'pop', 'pop']

Ouput:
4
5
6
5
EMPTY

Input:
string operations[n]: an array of string that represent operations on the stack
Ouput:
string: the value of the stack's top element; if the stack is empty, print "EMPTY"

TestCase 0:
operations = ['push 4', 'pop', 'push 3', 'push 5', 'push 2', 'inc 3 1', 'pop', 'push 1', 'inc 2 2', 'push 4', pop, pop]
Output:
4 EMPTY 3 5 2 3 6 1 1 4 1 8
"""

from collections import deque

class SuperStack():
    def __init__(self):
        self.stack = deque()
        self.offset = []

    def pop(self):
        p = self.offset.pop()
        if len(self.offset) > 0:
            self.offset[-1] += p
        return self.stack.pop() + p

    def push(self, element):
        self.stack.append(element)
        self.offset.append(0)

    def peek(self):
        if len(self.stack) == 0:
            return "EMPTY"
        return self.stack[-1] + self.offset[-1]

    def increment(self, numElements, amount):
        self.offset[numElements-1] += amount

    def runOp(self, opInfo):
        details = opInfo.split(" ")
        op = details[0]
        if op == "pop":
            return self.pop()
        elif op == "push":
            return self.push(int(details[1]))
        elif op == "inc":
            return self.increment(int(details[1]), int(details[2]))

    def runOperations(self, operations):
        for op in operations:
            self.runOp(op)
            print(self.peek())

def superStack(operations):
    ss = SuperStack()
    return ss.runOperations(operations)
