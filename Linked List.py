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

# Begining of code

List1 = LinkedList()

# Inserting elements into the list
List1.head = Node(5)
second = Node(10)
third = Node(15)

# Linking the Elements 
List1.head.next = second
second.next = third

List1.printList()