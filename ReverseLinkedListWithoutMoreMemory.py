class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.number_of_nodes = 0

    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.number_of_nodes += 1

    def count_of_nodes(self):
        return self.number_of_nodes

    def traverse(self):
        current_node = self.head

        while current_node is not None:
            print(f'{current_node.data} ->', end=' ')
            current_node = current_node.next_node
        print('None')

    def reverse(self):
        current_node = self.head
        next_node = None
        prev_node = None

        # 45 -> 35 -> 25 -> 15 -> 5
        while current_node is not None:
            # first pointing the next_node pointer to the actual next node (35)
            next_node = current_node.next_node
            # then change the pointer of the current node's next node to be previous node(here, None)
            current_node.next_node = prev_node
            # then, assign the previous node = current node (45)
            prev_node = current_node
            # then, Move ahead the current Node - by assigning next node to current node (35)
            current_node = next_node
            # this way -> after every iteration, current_node.next_node is pointing to prev_node,
            # and current_node and next node is pointing to same node ahead of the previous node

        self.head = prev_node


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.insert_beginning(5)
    linked_list.insert_beginning(15)
    linked_list.insert_beginning(25)
    linked_list.insert_beginning(35)
    linked_list.insert_beginning(45)

    linked_list.traverse()

    linked_list.reverse()
    print('After reversing the linkedlist')
    linked_list.traverse()
