class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, data):

        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
        self.count+=1
    def add_loop(self):

        n = 0
        rand = None
        curr = self.head
        while curr is not None:

            if n==4:
                rand = curr
            prev = curr
            curr = curr.next
            n+=1
            
        prev.next = rand
                
    def detect_loop(self):

        slow = self.head
        fast = self.head

        while slow is not None and fast is not None:
            slow = slow.next
            if fast.next is None:
                 break
            fast = fast.next.next
            
            if slow is fast:
                return True
        return False

    def find_middle(self):
        slow = self.head
        fast = self.head
        
        while slow is not None and fast is not None:
            slow = slow.next
            if fast.next is None:
                break
            fast = fast.next.next

        return slow.data
    def remove_loop(self):
        curr = self.head
        nodes = {}
        prev = None
        while curr is not None:
            
            if nodes.get(id(curr)) is None:
                nodes[id(curr)] = 1
            else:
                break
            prev = curr
            curr = curr.next
        prev.next = None

    def __len__(self):
        return self.count

    def rotate(self,k):
        parts = len(self)/k
        parts = parts+1 if parts%k !=0 else parts
        self.head = self.rotate_recur(self.head,k,parts)
        
    def rotate_recur(self,curr,k,parts):
        prev = None
        i = 0
        start = curr
        while i<k and curr is not None:
            nxt = None
            if curr.next is not None:
                nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            i+=1
            
        if curr is not None and parts>0:
            start.next = self.rotate_recur(curr,k,parts-1)
        return prev

    def sort(self):
        head =  self.head
        headzero = Node(1)
        headone = Node(2)
        headtwo = Node(3)
        zero = headzero
        one = headone
        two = headtwo
        curr = self.head
        while curr is not None:
            print(curr.data, id(curr))
            if curr.data == 0:
                
                zero.next = curr
                zero = zero.next                    
                curr = curr.next
                zero.next = None
            elif curr.data == 1:
                one.next =  curr
                one = one.next
                curr=curr.next
                one.next = None
            else:
                two.next = curr
                two = two.next
                curr = curr.next
                two.next = None
        print(headone.next.data)
        zero.next = headone.next
        one.next = headtwo.next
        print(headtwo.next.data)
        head.data = headzero.next.data
        head.next = headzero.next.next
        print(self.head.data)
                
        print(self.detect_loop())


    def __str__(self):
        curr = self.head
        nodes = []
        while curr is not None:
            print(curr.data)
            nodes.append(str(curr.data))
            curr = curr.next
        return ' -->'.join(nodes)

ll = LinkedList()
a = [1, 2, 2, 1, 2, 0, 2, 2]
for x in a:
    ll.add(x)

print(ll.find_middle())
    
ll.add_loop()
print(ll.detect_loop())
print(ll.remove_loop())
print(ll)
ll.sort()


