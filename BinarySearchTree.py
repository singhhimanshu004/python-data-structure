class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # We have to go to the left subtree
        if data < node.data:
            # left node exists: so we recursively call again the insert node function
            if node.left_node:
                self.insert_node(data, node.left_node)
            # there is no left node: so, we create a left node with the incoming data and parent node
            else:
                node.left_node = Node(data, node)
        # We have to go to the right subtree
        else:
            # right node exists, so, we recursively call again the insert node function
            if node.right_node:
                self.insert_node(data, node.right_node)
            # there is no right node: so, we create the right node with the incoming data and Node
            else:
                node.right_node = Node(data, node)

    def get_min(self):
        if not self.root:
            return None
        else:
            return self.get_min_value(self.root)

    def get_min_value(self, node):
        if node.left_node:
            return self.get_min_value(node.left_node)
        else:
            return node.data

    def get_max(self):
        if not self.root:
            return None
        else:
            return self.get_max_value(self.root)

    def get_max_value(self, node):
        if node.right_node:
            return self.get_max_value(node.right_node)
        else:
            return node.data

    def traverse(self):
        if self.root:
            return self.traverse_in_order(self.root)

        else:
            return None

    # it has O(N) linear running time complexity
    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)

        print(node.data, end=" ")

        if node.right_node:
            self.traverse_in_order(node.right_node)

    def remove(self, data):
        if self.root:
            return self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if not node:
            return
        if data < node.data:
            return self.remove_node(data, node.left_node)
        elif data > node.data:
            return self.remove_node(data, node.right_node)
        else:
            # We have found the node to be removed
            # There are 3 Options
            # LEAF NODE CASE
            if node.left_node is None and node.right_node is None:
                print(f"Removing a leaf Node: {node.data}")
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = None

                if parent is not None and parent.right_node == node:
                    parent.right_node = None

                if parent is None:
                    self.root = None

                del node
            # Node has One child
            elif node.left_node is None and node.right_node is not None:
                print(f"Removing a node with single right child: {node.data}")
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = node.right_node

                if parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node

                if parent is None:
                    self.root = node.right_node

                node.right_node.parent = parent
                del node

            elif node.right_node is None and node.left_node is not None:
                print(f"Removing a node with single left child: {node.data}")
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = node.left_node

                if parent is not None and parent.right_node == node:
                    parent.right_node = node.left_node

                if parent is None:
                    self.root = node.left_node

                node.left_node.parent = parent
                del node

            # Removing a node with both left child and right child
            elif node.left_node is not None and node.right_node is not None:
                # Note: 1. the smallest item in the right subtree is called the SUCCESSOR
                # Note: 2. the largest item in the left subtree is called the PREDECESSOR
                print(f"Removing a node with two children: {node.data}")
                # get the largest node in the left subtree
                predecessor = self.get_predecessor(node.left_node)
                # swap the node data with predecessor node data
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)
        return node


if __name__ == "__main__":
    bst = BST()
    bst.insert(35)
    bst.insert(27)
    bst.insert(76)
    bst.insert(56)
    bst.insert(12)
    bst.insert(32)
    bst.insert(97)

    print("Inorder traversal: (sorted order)")
    bst.traverse()
    print("\n")
    print(f"Min value in BST: {bst.get_min()}")

    print(f"Maxvalue in BST: {bst.get_max()}")

    bst.remove(56)
    bst.remove(97)
    bst.remove(76)
    print("Inorder traversal: (sorted order)")
    bst.traverse()
    print("\n")
    bst.remove(35)
    bst.remove(27)
    bst.remove(32)
    print("Inorder traversal: (sorted order)")
    bst.traverse()
    print("\n")
    bst.remove(12)
