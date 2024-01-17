class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, new_node):
        current = self.head

        if current:
            while current.next:
                current = current.next
            current.next = new_node
        
        else:
            self.head = new_node

    def delete(self, deleted_value):
        current = self.head

        if current.value == deleted_value:
            return
        else:
            while current:
                if current.value == deleted_value:
                    break
                else:
                    prev = current
                    current = current.next
            prev.next = current.next
            current = None

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


aa = Node(5)
b = Node(10)
c = Node(11)
ll = LinkedList(aa)
ll.append(b)
ll.append(c)
ll.delete(10)
ll.print()
ll.append(10)
ll.print()


