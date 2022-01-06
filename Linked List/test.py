from typing import List


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):

        temp = self.head

        if temp is None:
            print("The Linked List is empty")
        
        while temp is not None:
            print(temp.data, end = " ")
            temp = temp.next

    def add_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node

    def add_begining(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
    
    def add_pos(self,data,pos):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        if pos == 1:
            new_node.next = self.head
            self.head = new_node

            return

        pos -=1
        count = 1
        temp = self.head
        while count != pos:
            temp = temp.next
            count += 1

        new_node.next = temp.next
        temp.next = new_node    

        
            

    def countList(self):
        if self.head is None:
            count = 0
            print("There are ", count, " nodes in the list.")
            return

        count = 1
        temp = self.head
        while (temp.next):
            count += 1
            temp = temp.next

        print("There are ", count, " nodes in the list.")
    






# Begining of code

List1 = LinkedList()

# Inserting elements into the list
List1.head = Node(5)
second = Node(10)
third = Node(15)

# Linking the Elements 
List1.head.next = second
second.next = third

List1.add_end(100)
List1.add_begining(200)
List1.add_pos(300,1)

List1.countList()
List1.printList()