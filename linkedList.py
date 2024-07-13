#one can use this as a module by importing it and can help in solving the questions
#it Creates Single and Doubly Linked List
#It Involves Two Main Class SingleLL which creates the single Linked list and DoubleLL which creates the doubly linked list
#Each class has the following functions InsertAtBegining, InsertAtEnd, InsertAtPosition, Size, Printlist, DeleteByValue, DeleteAtEnd, DeleteAtBegining

class Node:
    def __init__(self,value):
        self.data=value #assigns the given data to the node
        self.next=None  #initialize the next attribute to null

class SingleLL:
    def __init__(self):
        self.head=None 

    def InsertAtBegining(self,new_data):
        new_node=Node(new_data) #creating new node by node class that we created in class node
        new_node.next=self.head
        self.head=new_node
    
    def InsertAtEnd(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node    

    def InsertAtPosition(self,val,index):
        NewNode=Node(val)
        if index==1:
            self.InsertAtBegining(val)
        else:
            temp=self.head
            for _ in range(index-2):
                if temp is None:
                    raise IndexError("index out of bound")
                temp=temp.next
            NewNode.next=temp.next
            temp.next=NewNode    

    def size(self):
        count=0
        temp=self.head
        while temp is not None:
            count+=1
            temp=temp.next
        return count if count>0 else 0  #this line beacuse it will not return integer value if the head in none    
    
    def DeleteAtBegining(self):
        if self.head is None:
            raise ValueError("add elements in the list")
            # print("add the elements")
        else:
            temp=self.head  #this is optional
            self.head=self.head.next
            temp.next=None #this is optional
            temp=None  #this is optional

    def DeleteAtEnd(self):
        if self.head is None:
            raise ValueError("NO ELEMENTS IN THE LINKED LIST")
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head 
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None      


    def DeleteAtPosition(self,index):
        if self.head is None:
            print("THE LIST IS EMPTY")
            return
        if index==1:
            self.head=self.head.next
            return
        temp=self.head
        prev=None
        for _ in range(index - 1):
            prev = temp
            temp = temp.next
            if not temp:
                print("Position out of bounds")
                return

        prev.next = temp.next
        temp.next = None            

    def DeleteByValue(self,val):
        if self.head is None:
           print("THE LIST IS EMPTY")
        elif self.head.data == val:
            self.head = self.head.next
        else:
           temp=self.head
           prev=None
           while temp is not None and temp.data is not val:
               prev=temp
               temp=temp.next
           if temp is None:    
               print(f'{val} not found') 
           else:
               prev.next=temp.next
               temp.next=None

    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data,"->",end=' ')
            temp=temp.next
        print("None")

class NodeDouble:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.previous=None

class DoubleLL:
    def __init__(self):
        self.head=None

    def InsertAtBegining(self,value):
        NewNode=NodeDouble(value)
        if self.head is None:
            self.head=NewNode
        else:
            NewNode.next=self.head
            self.head.previous=NewNode
            self.head=NewNode

    def InsertAtEnd(self,val):
        NewNode=NodeDouble(val)
        if self.head is None:
            self.head=NewNode
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=NewNode 
            NewNode.previous=temp        

    def InsertAtPosition(self,val,index):
        if self.head is None:
            print(f'{val} can not be entered as there are no elements in the Doubly linked list')
        elif index==1:
            self.InsertAtBegining(val)
        else:
            current=self.head
            for _ in range(index-2):
                if current is None:
                    print(f'{index} index is out of bound')
                    return
                current=current.next

            if current.next is None:
                self.InsertAtEnd(val)
            else:
                NewNode=NodeDouble(val)
                temp=current
                NewNode.next=current.next
                NewNode.previous=current
                current.next=NewNode
                temp.previous=NewNode

    def DeleteAtBegining(self):
        if self.head is None:
            print("No elements present to be deleted")
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None

    def size(self):
        count=0
        temp=self.head
        while temp is not None:
            count+=1
            temp=temp.next
        return count if count>0 else 0
    
    def DeleteAtEnd(self):
        if self.head is None:
            print("No elements present to be deleted")
            return
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None        

    def DeleteAtPosition(self,index):
        if self.head is None:
            print("Double Linked list empty")
            return
        else:
            current=self.head
            temp=None
            for _ in range(index-1):
                if current is None:
                    print(f'{index} index is out of bound')
                    return
                temp=current
                current=current.next
            temp.next=current.next
            current.next.previous=temp
            current.next=None
            current.previous=None

    def DeleteByValue(self,val):
        try:
             if self.head.value==val:
                 if self.head.next is not None:
                      self.head=self.head.next
                      self.head=None
                 else:
                     self.head=None     
             else:
                 temp=self.head.next    
                 while temp is not None and temp.value!=val:
                     temp=temp.next
                 if temp is None:
                     print(f'{val} is not present in the list')
                 else:
                     if temp.next is None: 
                        temp.previous.next=None
                     else:           
                        temp.previous.next=temp.next
                        temp.next.previous=temp.previous
                        temp.next=None
                        temp.previous=None    
        except:
            print("list is empty")


    def printLL(self):
        temp=self.head
        while temp is not None:
            print(temp.value,"->",end=" ")
            temp=temp.next
        print("None")    
