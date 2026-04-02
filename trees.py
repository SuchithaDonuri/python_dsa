# # A basic tree structure

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None          #Left child of the node Initially empty (None).
#         self.right=None         #Right child of the node Initially empty (None).


# node=Node(10)
# node.left=Node(5)
# node.right=Node(12)
# print(node.data)
# print(node.left.data)
# print(node.right.data)

from collections import deque

class Tree:    # creating a node of binary tree 
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

root=Tree(20)
root.left=Tree(12)
root.right=Tree(25)
root.left.left=Tree(9)
root.left.right=Tree(15)
root.right.left=Tree(21)
root.right.right=Tree(29)

#         20
#        /  \
#      12    25
#     /  \   / \
#    9   15 21 29


def max_depth(root):  # Function to calculate maximum depth (height) of the tree
    
    if not root:    #If tree is empty depth is 0 so we return 0
        return 0
    queue=deque([root])  # start bfs from root (starts from 20) queue=[20](initially)
    depth=0                 # stores no of levels initially it is 0


    while queue:            # loop runs until queue becomes empty (until all nodes are processed)
                            # one level for each iteration

        for i in range(len(queue)):         
            node=queue.popleft()            # Remove node from front of queue # node = 20(level 1),node = 12, 25 (level 2),node = 9,15,21,29 (level 3)
            
            if node.left:                   #if child exists add to the queue       
                queue.append(node.left)     #queue=[12],queue=[25,9],queue=[9,15,21]
            if node.right:
                queue.append(node.right)    #queue=[12,25],queue=[25,9,15],queue[9,15,21,29]

        depth+=1    # after finishing one level it increases the depth,(depth=1)(depth=2)(depth=3)

    print(depth)

max_depth(root)

    


        