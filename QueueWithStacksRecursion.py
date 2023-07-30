class Queue:
    def __init__(self):
        self.stack = []

    def enqueue(self, data):
        self.stack.append(data)

    # Dequeue using recursion
    def dequeue(self):
        if not self.stack:
            return -1
        # Base condition
        if len(self.stack) == 1:
            return self.stack.pop()

        item = self.stack.pop()

        dequeued_item = self.dequeue()
        # insert the item back in stack after the dequeued_item is found
        self.stack.append(item)

        return dequeued_item


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