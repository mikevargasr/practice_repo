from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)
    
    def peek(self):
        return self.container[-1]
    
    def pop(self):
        self.container.pop()

    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    def print_cont(self):
        return self.container
    

stack = Stack()
stack.push(5)
print(stack.peek())
stack.push(10)
stack.push(15)
print(stack.is_empty())
print(stack.print_cont())
