
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:


    
    def __init__(self):
        self.head = None
        self.size = 0
        self.mid = 0
        self.middle = None

    def add(self,data):

        if self.head is None:
            self.head = Node(data)
            self.middle = self.head
            self.size+=1
            self.mid+=1
            return
        else:
            node = Node(data)
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.size+=1
        mid = self.size/2
        print(mid)
        while int(mid) > self.mid:
            self.middle = self.middle.next
            self.mid+=1
            
            
            

    def remove(self,data):

        curr = self.head
        while curr is not None:
            if curr.data == data:
                if curr.prev is not None:
                    curr.prev.next = curr.next
                if curr.next is not None:
                    curr.next.prev = curr.prev
                break
            curr = curr.next
        self.size-=1
        mid = self.size/2
        while int(mid)<self.mid:
            self.middle = self.middle.prev
            self.mid-=1
        return curr.data


class Stack():

    def __init__(self):

        self.stack = DoublyLinkedList()


    def push(self,data):
        self.stack.add(data)
    def pop(self):
        return self.stack.remove(self.stack.head.data)
    def get_middle(self):
        if self.stack.middle is None:
            return None
        return self.stack.middle.data
    def delete_middle(self):
        return self.stack.remove(self.stack.middle.data)
            

        
