class BST():
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return

        if self.key == data:
            return
        
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                  self.rchild.insert(data)
            else:
                self.rchild = BST(data)
            

    def search(self, data):
        if self.key == data:
            print("Node found")
            return

        if data < self.key:
            if self.lchild:
               self.lchild.search(data)

            else:
                print("Node is not present in Tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("NOde is not present in Tree")

    def preorder(self):
        print(self.key, end = " ")

        if self.lchild:
            self.lchild.preorder()

        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()

        print(self.key, end = " ")

        if self.rchild:
            self.rchild.inorder()


    def postorder(self):
        if self.lchild:
             self.lchild.postorder()

        if self.rchild:
            self.rchild.postorder()

        print(self.key, end = " ")

    def delete(self, data,curr):
        if self.key is None:
            print("Three is emppty")
            return

        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Given Node is not present in the tree")

        elif data > self.key:
                if self.rchild:
                    self.rchild = self.rchild.delete(data)
                else:
                    print("Given Node is not present in the tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp

            if self.rchild is None:
                temp  = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
                self = None
                return temp

            node = self.rchild

            while node.lchild:
                node = node.lchild

            self.key = node.key  
            self.rchild = self.rchild.delete(node.key,0) 
            
        return self

    def minimum(self):
        current = self

        while current.lchild:
            current = current.lchild

        minn = current.key

        print()
        print("Mininum = ",minn)


    def maximum(self):
        current = self

        while current.rchild:
            current = current.rchild

        minn = current.key

        print()
        print("Maximum  = ",minn)
        
def count(node):
    if node is None:
        return 0
    else:
        return 1 + count(node.lchild) + count(node.rchild)
            
root = BST(20)
lst = [10, 4, 30, 4, 1 , 5, 6]

for i in lst:
    root.insert(i)

if count(root) > 1:
    root.delete(20,root.key)

print("PreOrder")
root.preorder()

print()
print()


print("Inorder")
root.inorder()

print()
print()

print("Postorder")
root.postorder()

root.minimum()
root.maximum()

print(count(root))






