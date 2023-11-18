stack=[]

def pop():
    if(len(stack)==0):
        print("Stack is empty.\n")
    
    else:
        print(f"poped element is: {stack.pop()}")
        print(stack)

def push(n):
    stack.append(n)
    print(stack)
    
def display():
    if(len(stack)==0):
        print("Stack is empty.\n")
    else:
       print(stack)
       print(f"length of stack is: {len(stack)}")
    
def top_element():
    if(len(stack)==0):
        print("Stack is empty.\n")
    else:
        print(stack[-1])
            
        
def bottom_element():
    if(len(stack)==0):
        print("stack is empty.")
    else:
        print(stack[0])

a=int(input(f"\n--> enter: \n\t1. push \n\t2. pop\n\t3. Display\n\t4.top element\n\t5. bottom element   \n"))
if(a==1):
    s=int(input(f"Enter the size of stack: "))
    for i in range(s+1):
        n=int(input("enter the number: "))
        push(n)

elif(a==2):
    pop()

elif(a==3):
    display()
elif(a==4):
    top_element()
elif(a==5):
        bottom_element()
