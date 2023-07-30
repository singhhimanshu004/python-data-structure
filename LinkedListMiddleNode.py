class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # O(N) linear running time complexity
    def get_middle_node(self):
        # if self.size == 0:
        #     return None
        # if self.size % 2 == 0:
        #     index_counter = self.size // 2
        # else:
        #     index_counter = self.size // 2 + 1
        #
        # counter = 1
        # actual_node = self.head
        # while (counter != index_counter):
        #     actual_node = actual_node.next_node
        #     counter += 1
        #
        # return actual_node
        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer

    def insert(self, data):

        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def traverse_list(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next_node


if __name__ == '__main__':

    linked_list = LinkedList()

    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    linked_list.insert(40)
    linked_list.insert(50)
    print(linked_list.get_middle_node().data)
