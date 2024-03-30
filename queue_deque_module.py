
from collections import deque

queue = deque()
queue.append(1)  # enqueue
front_element = queue.popleft()  # dequeue
front_element = queue.popleft()
print(front_element)  # Output: 1
print(len(queue))


