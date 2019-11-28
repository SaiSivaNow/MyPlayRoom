class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None


class BinarySearchTree:
    def __init__(self):
        self.root=None

    def add(self,data):
        self.root=self.addNode(data,self.root)

    def addNode(self,data,node):
        if node==None:
            return Node(data)
        elif data<node.data:
            node.left=self.addNode(data,node.left)
        elif data>= node.data:
            node.right=self.addNode(data,node.right)
        return node

    def inorder(self):
        self.inorderNode(self.root)

    def inorderNode(self,node):

        if node == None:
            return

        self.inorderNode(node.left)
        print(node.data)
        self.inorderNode(node.right)

    def preorder(self):
        yield self.preorderNode(self.root)

    def preorderNode(self,node):
        if node==None:
            return
        yield node.data
        self.preorderNode(node.left)
        self.preorderNode(node.right)

    def height(self):
        return self.heightNode(self.root)

    def heightNode(self,node):
        if node==None:
            return 0
        else :
            return max(self.heightNode(node.left),self.heightNode(node.right))+1

    def nthlevel(self,n):
        self.levelorderNode(self.root,n)

    def levelorderNode(self,node,level):
        if(level==1):
            print(node.data)
        else :
            self.levelorderNode(node.left,level-1)
            self.levelorderNode(node.right,level-1)

    def nthlevelsum(self,n):
        max_height=self.height()
        if(n<=max_height):
            print(self.nthlevelsumNode(self.root,n))
        else:
            print('Max level existing',max_height)
        

    def nthlevelsumNode(self,node,level):
        if level==1 or level==0:
            return node.data
        else :
            return self.nthlevelsumNode(node.right,level-1)+self.nthlevelsumNode(node.left,level-1)

        
class AVLTree(BinarySearchTree):

    def right_rotate(self,node):
        
        temp = node.left
        node.left = temp.right
        temp.right = node

        return temp

    def left_rotate(self,node):

        temp = node.right
        node.right = temp.left
        temp.left = node

        return temp

    def get_balance(self,node):

        return self.heightNode(node.left)-self.heightNode(node.right)

    def addNode(self,data,node):

        if node == None:
            return Node(data)

        if data < node.data :
            node.left = self.addNode(data,node.left)

        if data >= node.data:
            node.right = self.addNode(data,node.right)


        balance = self.get_balance(node)

        #left-left case --> right rotate
        if balance > 1 and data < node.left.data :
            return self.right_rotate(node)

        #left-right case --> left right rotate
        if balance > 1 and data > node.left.data :
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        #right-right case --> left rotate

        if balance < -1 and data > node.right.data:
            return self.left_rotate(node)

        #right - left case --> right left rotate

        if balance < -1 and data < node.right.data:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node
            
    

        



        

        
        
