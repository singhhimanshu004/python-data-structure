CAPACITY = 10
# Max heap


class Heap:
    def __init__(self):
        # this is the actual number of items in the data structure
        self.heap_size = 0
        # the underlying heap data structure
        self.heap = [0] * CAPACITY

    def insert(self, item):
        # If heap is full
        if self.heap_size == CAPACITY:
            return

        self.heap[self.heap_size] = item
        self.heap_size += 1

        # check heap properties
        self.fix_up(self.heap_size - 1)

    # starting with actual node we have inserted up to the root node, we have to
    # compare the values whether to make swap operation.
    # It has O(logN) running time complexity
    def fix_up(self, index):
        # l = 2i +1
        # r = 2i +2
        parent_index = (index - 1) // 2

        # we consider all the items above till we hit root node.
        # if heap property is violated, then we swap the parent child
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[index],
            )
            self.fix_up(parent_index)

    # peek() - return with the max item in O(1)
    def get_max(self):
        return self.heap[0]

    # remove the max and removes it as well
    # remove the root node of the heap and then heapify the remaining heap
    def poll(self):
        max_item = self.get_max()

        # swap the root node with the last node and then "heapify"
        self.heap[0], self.heap[self.heap_size - 1] = (
            self.heap[self.heap_size - 1],
            self.heap[0],
        )
        self.heap_size = self.heap_size - 1

        self.fix_down(0)

        return max_item

    # starting with the root node downwards until the heap properties
    # are not violated
    def fix_down(self, index):
        index_left = 2 * index + 1
        index_right = 2 * index + 2

        # In a max heap the parent is always greater than the children
        largest_index = index

        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            largest_index = index_left

        if (
            index_right < self.heap_size
            and self.heap[index_right] > self.heap[largest_index]
        ):
            largest_index = index_right
        # if the parent is larger than the children: it is valid heap so we terminate
        # the recursive function calls
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = (
                self.heap[largest_index],
                self.heap[index],
            )
            self.fix_down(largest_index)

    def heap_sort(self):
        for _ in range(self.heap_size):
            max_val = self.poll()
            print(max_val)


if __name__ == "__main__":
    heap = Heap()
    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(8)
    heap.insert(1)
    heap.insert(-5)
    heap.insert(99)

    print(heap.heap)

    print("Sorted after heap sort: \n ")
    print(heap.heap_sort())
