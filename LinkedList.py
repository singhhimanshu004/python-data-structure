import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        # this is the first node of the linked list
        # We can access this exclusively.
        self.head = None
        self.num_of_nodes = 0

    def size_of_list(self):
        return self.num_of_nodes

    def insert_beginning(self, data):
        # O(1) as only updating the references
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # O(1)
        if self.head is None:
            self.head = new_node

        else:
            actual_node = self.head
            # Bottle neck ( takes O(N))
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node
            actual_node.next_node = new_node

    def traverse(self):
        # O(N) as linear traversal!!
        actual_node = self.head
        while actual_node is not None:
            # The print method takes an extra parameter end=" " to keep the pointer on the same line
            print(f'{actual_node.data} ->', end=' ')
            actual_node = actual_node.next_node
        print('None')

    def remove(self, data):
        # Empty list
        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        # search miss
        if previous_node is None:
            return

        # data found - removing in O(N)
        else:
            print(f'removing Node \'{actual_node.data}\'')
            previous_node.next_node = actual_node.next_node
            self.num_of_nodes -= 1
            return


if __name__ == '__main__':
    # Initialise the linked list first!!
    linked_list = LinkedList()

    linked_list.insert_beginning(5)
    linked_list.insert_beginning('Adam')
    linked_list.insert_end(7.5)
    linked_list.insert_beginning('shubhangi')
    linked_list.insert_end('himanshu')
    linked_list.insert_end(1000)
    linked_list.traverse()
    print(f'size of linked list: {linked_list.size_of_list()}')

    print('-----------')

    linked_list.remove(7.5)
    linked_list.remove('Adam')
    linked_list.remove(1000)
    linked_list.traverse()
    print(f'size of linked list: {linked_list.size_of_list()}')

    # comparison between Python list and LinkedList insertion time
    # now = time.time()
    # for i in range(500000):
    #     linked_list.insert_beginning(i)
    # print(f'time taken to insert data in linkedlist: {time.time() - now}')
    #
    # array = []
    #
    # now = time.time()
    # for i in range(500000):
    #     array.insert(0, i)
    #
    # print(f'time taken to insert data in array: {time.time() - now}')
