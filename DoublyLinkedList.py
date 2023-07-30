class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.number_of_nodes = 0

    def size_of_list(self):
        return self.number_of_nodes

    # insert in O(1) (at the end)
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # else, There exist at least one node in the linked list
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def traverse(self):
        actual_node = self.head
        print('From Head: ', end=' ')
        while actual_node is not None:
            print(f'{actual_node.data} ->', end=' ')
            actual_node = actual_node.next_node
        print('None')

    def reverse_traverse(self):
        actual_node = self.tail
        print('From Tail: ', end=' ')
        while actual_node is not None:
            print(f'{actual_node.data} ->', end=' ')
            actual_node = actual_node.prev_node
        print('None')


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert(5)
    doubly_linked_list.insert(8)
    doubly_linked_list.insert(98)
    # Visualization:
    # head -> 5 -> 8 -> 98 -> None
    # None <- 5 <- 8 <- 98 <- tail
    print('------TRAVERSAL------')
    doubly_linked_list.traverse()

    print('------REVERSE TRAVERSAL-------')
    doubly_linked_list.reverse_traverse()
