#!/bin/python3

import os
import sys
import queue

#
# Complete the swapNodes function below.
#

class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    
    def __init__(self):
        self.root = Node(1)
        self.nodes =[self.root]
    def add(self, parent, data):
        if data[0] !=-1:
            self.nodes[parent].left =  Node(data[0])
            self.nodes.append(self.nodes[parent].left)
        if data[1] !=-1:
            self.nodes[parent].right = Node(data[1])
            self.nodes.append(self.nodes[parent].right)
    

    def swap_nodes(self, k):
        q = queue.Queue()
        q.put(self.root)
        level = 1
        while True:
            if q.empty():
                break
            nodes = q.qsize()
            while nodes>0:
                curr = q.get()
                if level == k:
                    temp =  curr.right
                    curr.right = curr.left
                    curr.left = temp
                if curr.left is not None:
                    q.put(curr.left)
                if curr.right is not None:
                    q.put(curr.right)
                nodes-=1
            if level == k:
                k+=k
            level+=1
            
        return self.inorder()

    def inorder(self):
        inor = []
        self.inorder_recur(self.root,inor)
        return inor
    def inorder_recur(self, node,inor):

        stack = [self.root]

        while len(stack) != 0:
            if stack[-1].left is not None:
                stack.append(stack[-1].left)
                continue
            parent = stack.pop()
            inor.append(parent.data)
            if parent.right is not None:
                stack.append(parent.right)
            elif len(stack)!=0 :
                parent = stack.pop()
                inor.append(parent)
                stack.append(parent.right)
            
            

    


def swapNodes(indexes, queries):
    #
    # Write your code here.
    #
    tree =  Tree()
    for x in range(0,len(indexes)):
        tree.add(x,indexes[x])
    result = []
    for query in queries:
        result.append(tree.swap_nodes(query))

    return result
if __name__ == '__main__':

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)
