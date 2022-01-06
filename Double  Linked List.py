class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            new_node.prev = temp
            temp.next = new_node

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty.")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, "--> ", end=" ")
                temp = temp.next


dll = DoubleLinkedList()
dll.add_end(3000)
dll.print_LL()
