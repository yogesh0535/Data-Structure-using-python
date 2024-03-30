class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
    
class linklist:
    def __init__(self) -> None:
        self.head=None
    
    def insert(self,data):
        new_nod=Node(data)
        new_nod.next=self.head
        self.head=new_nod
        
    def traversal(self):
        current=self.head
        while current != None:
            print(current.data)
            current=current.next
            
            
    def insert_end(self,data):
        current=self.head
        new_node=Node(data)
        while current.next != None:
            current=current.next
        
        current.next=new_node
        
    
    def insert_middle(self,data,value):
        new_nod=Node(data)
        current_node=self.head
        
        while current_node.next != None:
            if current_node.data == value:
                new_nod.next=current_node.next
                current_node.next=new_nod
            current_node=current_node.next
            
            
            

        
        
l=linklist()
l.insert(6)
l.insert(4)
l.insert(7)

l.insert_end(8)
l.insert_end(9)

l.traversal()

l.insert_end(10)
l.traversal()

l.insert_middle(1,8)
l.insert_middle(5,4)

l.traversal()