queue=[]

while(True):
    def enqueue(n):
        queue.append(n)

    def dequeue():
        if len(queue) == 0:
            print("queue is empty.")
        else:
            return queue.pop(0)

    def print_queue():
        if len(queue) == 0:
            print("queue is empty.")
        else:
            print(queue)

    def top_elements():
        if len(queue) == 0:
            print("queue is empty.")
        else:
            print(f"first element is: {queue[0]}")
            print(f"last element is: {queue[-1]}")


    def queue_reverse():
        queue.reverse()
        print(queue)



    print(f"\n\n1.push\n2.pop\n3.Display\n4.top element\n5.queue reverse")
    a=int(input("enter your choice: "))

    if (a==1):
        n=int(input("enter the number: "))
        enqueue(n)

    elif (a==2):
        dequeue()
        print(f"poped element is: {dequeue()}")


    elif (a==3):
        print_queue()

    elif (a==4):
        top_elements()

    elif (a==5):
        queue_reverse()
        
    else:
        print("invalid choice")
