class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        if self.dequeue_stack:
            return self.dequeue_stack.pop()

        elif not self.enqueue_stack:
            return -1

        else:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()

    def size_of_queue(self):
        return len(self.enqueue_stack) + len(self.dequeue_stack)

    def is_empty(self):
        return self.enqueue_stack == [] and self.dequeue_stack == []


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(45)
    queue.enqueue(55)
    queue.enqueue(65)

    print(queue.dequeue())

    queue.enqueue(100)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())