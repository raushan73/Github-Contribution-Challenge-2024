# Program: Implement a stack using a list and define push, pop, and isEmpty methods.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None

    def isEmpty(self):
        return len(self.stack) == 0

# Test case
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Expected output: 2
