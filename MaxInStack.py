class Stack:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def push(self, data):
        self.main_stack.append(data)
        if len(self.main_stack) == 1:
            self.max_stack.append(data)

        elif data > self.max_stack[-1]:
            self.max_stack.append(data)

        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        data = self.main_stack[-1]
        del self.main_stack[-1]
        del self.max_stack[-1]
        return data

    def peek(self):
        return self.main_stack[-1]

    def max_item(self):
        return self.max_stack[-1]

    def size_of_stack(self):
        return len(self.main_stack)


if __name__ == '__main__':
    stack = Stack()
    stack.push(97)
    stack.push(64)
    stack.push(198)
    stack.push(37)

    print(f'max item: {stack.max_item()}')

    print(f'popped item: {stack.pop()}')

    print(f'max item: {stack.max_item()}')

    print(f'popped item: {stack.pop()}')

    print(f'max item: {stack.max_item()}')
