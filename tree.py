class Node:
    def __init__(self,data) -> None:
        self.left=None
        self.right=None
        self.data=data
        
    def insert(self,data):
        if self.data:
            if data == self.data:
                return
            
            if data < self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
                
            else:
                if self.right is None:
                    self.right = Node(data)
                    
                else: 
                    self.right.insert(data)
        else:
            self.data=data
    
    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        
        if self.right:
            self.right.preorder()
    
    def inorder(self):
        if self.left:
            self.left.inorder()
        
        print(self.data)
        
        if self.right:
            self.right.inorder()
            
    def postorder(self):
        if self.left:
            self.left.postorder()
        
        if self.right:
            self.right.postorder()
        print(self.data)
    
    
    def search(self,value):
        if self.data:
            if self.data == value:
                print("Node is found!")
        
            if value<self.data:
                if self.left:
                    self.left.search(value)
                
                else:
                    print("Node is not present in tree!")
            
            if value> self.data:
                if self.right:
                    self.right.search(value)
                else:
                    print("Node is not found in tree!")
    
    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()
    
    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()
    
    def delete(self,value):
        
        if value<self.data:
            if self.left:
                self.left.delete(value)
            
        elif value>self.data:
            if self.right:
                self.right.delete(value)
        
        else:
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            
            if self.right is None:
                return self.left
        
            min_value=self.right.min()
            self.data=min_value
            self.right = self.right.delete(min_value)
        
        # return self
            

            

tree=Node(10)
list=[23,4,45,4,67,3,2,10]
for i in list:
    tree.insert(i)

print("/nPreorder:")
tree.preorder()

print("/nInorder: ")
tree.inorder()

print("/npostorder: ")
tree.postorder()

tree.search(00)
print("Mini and max are: ")
print(tree.min())
print(tree.max())
tree.inorder()
tree.delete(4)
tree.inorder()
