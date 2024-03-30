import heapq

queue = []
heapq.heappush(queue, (1, 'task1'))  # enqueue with priority
heapq.heappush(queue, (3, 'task3'))
heapq.heappush(queue, (2, 'task2'))
priority, task = heapq.heappop(queue)  # dequeue with highest priority

print(task)
from queue import PriorityQueue

queue = PriorityQueue()
queue.put((1, 'task1'))  # enqueue with priority
queue.put((3, 'task3'))
queue.put((2, 'task2'))
priority, task = queue.get()  # dequeue with highest priority
print(task)
print(queue)