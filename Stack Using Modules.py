import queue, collections

# stack = queue.LifoQueue(3)
# stack.put(30)
# stack.put(40)
# stack.put(50)
#
# stack.put(80, timeout=1)

stack1 = collections.deque()

stack1.append(10)
stack1.append(20)
stack1.append(30)

stack1.pop(30)