class Queue:

    def __init__(self):
        self.ds = []
        self.front = 0

    def deque(self):
        x = self.ds[self.front]
        del self.ds[self.front]
        return x
    def enque(self,data):
        self.ds.append(data)

    def __len__(self):
        return len(self.ds)

class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):

        self.root = None

    def add(self, data):

        self.root = self.add_node(self.root,data)

    def add_node(self,node,data):

        if node is None:
            return Node(data)

        if data <= node.data:
            node.left = self.add_node(node.left,data)
        else:
            node.right = self.add_node(node.right,data)
        return node


    def inorder_next_node(self, node):

        if node.left is None:
            return node
        if node.left is not None:
            return self.inorder_next_node(node.left)

    def delete(self, data):

        self.root = self.delete_node(self.root, data)


    def delete_node(self, node, data):

        if node.data == data:
            if node.left is None and node.right is None:
                return None
            elif node.left is not None and node.right is not None:
                 next_node = self.inorder_next_node(node.right)
                 node.data = next_node.data
                 node.right = self.delete_node(next_node,next_node.data)
            elif node.left is not None:
                node.data = node.left.data
                node.left = self.delete_node(node.left,node.left.data)
            elif node.right is not None:
                node.data = node.right.data
                node.right = self.delete_node(node.right,node.right.data)
        elif node.data < data:
            node.right = self.delete_node(node.right,data)

        elif node.data > data:
            node.left = self.delete_node(node.left,data)

        return node

    def level_order(self):

        q = Queue()
        q.enque(self.root)
        level = 0
        while True:
            level+=1
            nodecount = len(q)
            if nodecount == 0:
                break
            print("Level "+level)
            while nodecount!=0:
                curr = q.deque()
                print(curr.data)
                if curr.left is not None:
                    q.enque(curr.left)
                if curr.right is not None:
                    q.enque(curr.right)
                nodecount-=1
            
                    

        
                
    def inorder(self):
        stack = []

        stack.append(self.root)

        while len(stack) !=0:

            node = stack.pop()
            if node.right is None and node.left is None:
                print(node.data)
                continue
            if node.right is not None:
                stack.append(node.right)
                node.right = None
            temp = node.left
            node.left = None
            stack.append(node)
            if temp is not None:
                stack.append(temp)
                
    def preorder(self):

        stack = []
        stack.append(self.root)
        while len(stack) !=0:
            node = stack.pop()
            if node.right is None and node.left is None:
                print(node.data)
            left = node.left
            right = node.right
            node.left  = None
            node.right = None
            if right is not None:
                stack.append(right)
            if left is not None:
                stack.append(left)
            stack.append(node)
    def print(self):
        self.printNode(self.root)

    def printNode(self,node):

        if node is None:
            return
        self.printNode(node.left)
        print(node.data)
        self.printNode(node.right)

        
              
                
                 
        
