from collections import deque
'''
A double-ended queue, or deque, is 
a queue that allows insertion and deletion of elements at both ends. It can function as
both a queue and a stack, providing flexibility in accessing and manipulating elemen
'''

deque = deque()
deque.append(1)  # enqueue at rear
deque.appendleft(2)  # enqueue at front
print(deque)
front_element = deque.popleft()  # dequeue from front
rear_element = deque.pop()  # dequeue from rear
print(front_element)
print(rear_element)