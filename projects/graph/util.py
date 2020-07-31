
# Note: This Queue class is sub-optimal. Why?

# for queue we're appending, so we're backing this with an array so we
# enqueue: append (goes to the back)
# comes in from the right to come out to the left
# so when we pop from the left in a queue (first),
# it's addressing right at that exact spot (chunk of cells in one slot of memory)

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)
