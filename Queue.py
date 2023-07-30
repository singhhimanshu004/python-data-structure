# FIRST IN FIRST OUT: FIFO
# Abstract data type

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    # O(N) run time complexity - how to solve this? Use doubly linked list to implement this.
    # That will reduce the runtime complexity to O(1)
    def dequeue(self):
        if not self.queue:
            return -1
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        if not self.queue:
            return -1
        return self.queue[0]

    def is_empty(self):
        return self.queue == []

    def size_of_queue(self):
        return len(self.queue)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(15)
    queue.enqueue(25)
    queue.enqueue(35)
    queue.enqueue(45)
    queue.enqueue(55)

    print(f'size of queue: {queue.size_of_queue()}')
    print(f'dequeued value: {queue.dequeue()}')

    print(f'size of queue: {queue.size_of_queue()}')
    print(f'dequeued value: {queue.dequeue()}')

    print(f'size of queue: {queue.size_of_queue()}')
    print(f'dequeued value: {queue.dequeue()}')

    print(f'size of queue: {queue.size_of_queue()}')
    print(f'peeked value: {queue.peek()}')

    print(f'size of queue: {queue.size_of_queue()}')

    print(f'dequeued value: {queue.dequeue()}')
    print(f'dequeued value: {queue.dequeue()}')
    print(f'dequeued value: {queue.dequeue()}')
    print(f'dequeued value: {queue.dequeue()}')
    print(f'dequeued value: {queue.dequeue()}')
    print(f'dequeued value: {queue.dequeue()}')