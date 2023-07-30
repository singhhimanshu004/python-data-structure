# LAST IN LAST OUT (LIFO)
# Abstract data type
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            return -1
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        if len(self.stack) < 1:
            return -1
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def size_of_stack(self):
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack()
    stack.push(5)
    stack.push(15)
    stack.push(25)
    stack.push(35)
    stack.push(45)

    print(f'Popped data: {stack.pop()}')
    print(f'size of stack: {stack.size_of_stack()}')
    print(f'Popped data: {stack.pop()}')
    print(f'size of stack: {stack.size_of_stack()}')
    print(f'Popped data: {stack.pop()}')
    print(f'size of stack: {stack.size_of_stack()}')
    print(f'Peeked Value: {stack.peek()}')
    print(f'size of stack: {stack.size_of_stack()}')
