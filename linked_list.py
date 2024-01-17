class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data =  data
        self.next = next
        self.prev=prev

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data=data, next=self.head,prev=None)
        self.head=node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None,itr)

    def print_forward(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        llstring = ""

        while itr:
            llstring += str(itr.data) + '-->'
            itr = itr.next
        
        print(llstring)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        llstring = ""

        back_node = self.get_last_node()

        while back_node:
            llstring += str(back_node.data) + '-->'
            back_node = back_node.prev

        print(llstring)


    def get_last_node(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr


    def insert_values(self, datalist):
        for data in datalist:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head

        while itr.next:
            itr = itr.next
            count += 1

        return count
    
    def remove_at(self, index):
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1
            
    def insert_at(self, index, value):
        if index<0 or index>self.get_length(): 
            raise Exception("Invalid Index")
        
        if index==0:
            self.insert_at_beginning(value)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(value, itr.next, itr)
                itr.next = node
                break

            itr = itr.next
            count += 1
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(18)
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_values(["bananas","apple"])
    ll.remove_at(6)
    ll.remove_at(5)
    ll.insert_at(2, 15)
    ll.insert_at(4, 2)
    ll.insert_at_end(20)
    ll.insert_values([3,4,6])
    ll.print_forward()
    ll.print_backward()
