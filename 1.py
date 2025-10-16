from collections import deque
# Stack (LIFO)
stack=deque()
stack.append('a')
stack.append('b')
stack.append('c')
print("Stack:",stack)
stack.pop()
print("After pop(stack):",stack)

#Queue
queue=deque()
queue.append('x')
queue.append('y')
queue.append('z')
print("Queue",queue)
queue.popleft()

