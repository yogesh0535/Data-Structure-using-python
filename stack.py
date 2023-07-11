class stack:
    def __init__(self):
        self.data=[]
    
    
    # adding data in stack
    def push(self,data):
        self.data.append(data)
    
    def delete(self):
        l=len(self.data)
        if (l == 0):
            print("Stack is empty")
        else:
            print(f"poped element is:{self.data.pop()}")
        
    
    def lenght(self):
        print(f"lenght of stack is : {len(self.data)}")

    def empty(self):
        return len(self.data)==0
    
    def display(self):
        l=len(self.data)
        if (l == 0):
            print("Stack is empty")
        
        else:
            print(f"elements are: {self.data}")
    def top(self):
        l=len(self.data)
        if (l == 0):
            print("Stack is empty")
        else:
            print(f"top element is: {self.data[-1]}")
         
s=stack()
s.push(5)
s.push(9)
s.push(7)
s.push(6)
s.display()
s.delete()
s.display()
s.lenght()
print(s.empty())
s.top()
