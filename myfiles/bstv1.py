class Node():

    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None


class BST():
    _mirroroot=None
    def __init__(self):
        self.root=None
        
    def addBST(self,data,node):
        if node==None:
            return Node(data)
        if data<node.data:
            node.left=self.addBST(data,node.left)
        elif data>node.data:
            node.right=self.addBST(data,node.right)

        return node

    def add(self,data):
        self.root=self.addBST(data,self.root)
        
    

    def preorder(self):
        self.preorderBST(self.root)

    def preorderBST(self,node):
        if node==None:
            return
        
        self.preorderBST(node.left)
        self.preorderBST(node.right)
        print(node.data)

    def height(self):
        return self.heightBST(self.root)
    def heightBST(self,node):
        if node==None:
            return 0
        return 1+max(self.heightBST(node.left),self.heightBST(node.right))
    def mirror(self):
        self._mirrorroot=self._mirror(self.root)
        inorder(self._mirrorroot)

    def _mirror(self,node):
        if node is None:
            return None
        left=node.left
        right=node.right
        if left is None and right is None:
            return node

        if left is not None:
            node.right=self._mirror(left)

        if right is not None:
            node.left=self._mirror(right)

        return node
        

        
    

        
        
