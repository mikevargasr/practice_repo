from collections import deque

class Queue:
    #CODE WITH DEQUE
    
    # def __init__(self):
    #     self.container = deque()

    # def enqueue(self, value):
    #     self.container.appendleft(value)

    # def remove(self):
    #     self.container.pop()
    
    # def is_empty(self):
    #     return len(self.container) == 0
    
    # def size(self):
    #     return len(self.container)

    # CODE WITH NO PACKAGES
    def __init__(self):
        self.container = []
    
    def enqueue(self, value):
        self.container.insert(0, value)

    def remove(self):
        self.container.pop()
    
    def size(self):
        return len(self.container)
    
    def is_empty(self):
        return len(self.container) == 0
    
    
q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
q.remove()
print(q.size())
print(q.container)