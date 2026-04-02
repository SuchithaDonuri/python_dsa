# Node structure in LL
#creating a node 

# class Node:
#     def __init__(self,data):
#         self.data=data  # to store the value
#         self.next=next  # pointer to the next node (initially none)
        

# #creating the linked list

# class LinkedList:

#     def __init__(self):
#         self.head=None

#     def insert(self,data):
#         new_node=Node(data) # creating a new node
#         if not self.head:
#             self.head=new_node
#             return
#         temp=self.head
#         while temp.next:  # traverse to the last node
#             temp=temp.next
#         temp.next=new_node


#     def display(self):
#         temp=self.head
#         while temp:
#             print(temp.data,end="->")
#             temp=temp.next
#         print("None")

        
# l1=LinkedList()
# l1.insert(10)
# l1.insert(20)
# l1.insert(30)
# l1.display()

# singly linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class SingleLinkedList:
#     def __init__(self):
#         self.head=None

#     def display(self):
#         temp=self.head
#         result=[]
#         while temp:
#             result.append(temp.data)
#             temp=temp.next
#         print("LinkedList",result)

#     def insert(self,data):
#         new_node=Node(data)
#         if not self.head:
#             self.head=new_node
#             return
#         temp=self.head
#         while temp.next:
#             temp=temp.next
#         temp.next=new_node

#     def delete(self,key):
#         temp=self.head      #saving head in temp variable
        
#         #case1 if key means the node to be deleted in head
#         if temp and temp.data==key:
#             self.head=temp.next     #adding next element to the head like making next element as head
#             temp=None               # deleting temp
#             return
        
#         #case2 if the key is not head and somewhere in the middle of the list
#         prev=None
#         while temp and temp.data != key:
#             prev=temp
#             temp=temp.next

#         #case3 if the key is not present in the list (node to be deleted)
#         if temp is None:
#             return
        
#         #to delete the node
#         prev.next=temp.next         #removing the temp and making link to the prev node and next node (the node after deleted node)
                                  
#         temp=None



# ll=SingleLinkedList()
# ll.insert(10)
# ll.insert(20)
# ll.insert(30)
# ll.insert(40)
# ll.insert(50)
# ll.insert(60)
# ll.display()
# ll.delete(30)
# ll.display()
# ll.delete(90)
# ll.display()


# for i in range(0,21):
#     print(i)
    
# for j in range(0,21,2):
   
#     print(j)



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None
    
#     def append(self,data):
#         new_node=Node(data)  #node(1),node(2),node(3),node(5)

#         if self.head is None:
#             self.head=new_node #self.head=1 
#             return
        
#         temp=self.head      #temp=1

#         while temp.next:
#             temp=temp.next      #temp=2,temp=3,temp=4

#         temp.next=new_node      #temp.next=2 temp.next=3,temp.next=4,temp.next=5

# ll=LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.append(5)
        
# # Linked Lists:
# Q1 — Find Middle of Linked List
# Find the middle node of a linked list in one pass (without counting length first).

# Input : 1 → 2 → 3 → 4 → 5 → None
# Output: Middle node is 3

# Input : 1 → 2 → 3 → 4 → None
# Output: Middle node is 3

# class Node:
#     def __init__(self,data):        
#         self.data=data          #[data = 10 | next = None]
#         self.next=None



# class LinkedList:

#     def __init__(self):
#         self.head=None      # initially the head will be none

#     def append(self,data):
#         new_node=Node(data)

#         if self.head is None:
#             self.head=new_node
#             return
        
#         temp=self.head
#         while temp.next:
#             temp=temp.next

#         temp.next=new_node

#     def find_middle(self):
#         fast=self.head  # Both start at head
#         slow=self.head

#         while fast is not None and fast.next is not None: # loop runs until fast reaches end
#             slow=slow.next
#             fast=fast.next.next

#         return slow
    
# ll=LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# # ll.append(5)
# middle=ll.find_middle()
# print(f"Middle node is {middle.data}")




# # Q2 — Reverse a Linked List
# # Reverse a singly linked list in place.

# # Input : 1 → 2 → 3 → 4 → 5 → None
# # Output: 5 → 4 → 3 → 2 → 1 → None

# class Node:
#     def __init__(self,data):        
#         self.data=data          #[data = 10 | next = None]
#         self.next=None


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None   


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         temp = self.head
#         while temp.next:
#             temp = temp.next

#         temp.next = new_node

   
#     def reverse(self):
#         prev = None
#         curr = self.head

#         while curr:
#             next_node = curr.next   # step 1: save next 2 ,3,4,5
#             curr.next = prev        # step 2: reverse link None ,1,2,3
#             prev = curr             # step 3: move prev 1 ,2,3,4
#             curr = next_node        # step 4: move curr 2,3,4,5

#         self.head = prev   # None 

   
#     def print_list(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" → ")
#             temp = temp.next
#         print("None")



# ll = LinkedList()

# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.append(5)

# print("Original List:")
# ll.print_list()

# ll.reverse()

# print("Reversed List:")
# ll.print_list()


# insert at beginning of the linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        new_node=Node(data,self.head)
        self.head=new_node

    def print(self):
        if not self.head:
            self.print("Linked list is empty")
            return
        temp=self.head
        llstr=""

        while temp:
            llstr+=str(temp.data) + '--->'
            temp=temp.next

        print(llstr)


ll=LinkedList()
ll.insert_at_begining=Node(20)
# ll.insert_at_begining(30)
ll.print()



        
        