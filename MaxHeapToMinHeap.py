class HeapTransformer:
    def __init__(self, heap):
        self.heap = heap

    def transform(self):
        for i in range((len(self.heap) - 2) // 2, -1, -1):
            self.fix_down(i)
        # your implementation here

    def fix_down(self, index):
        index_left = 2 * index + 1
        index_right = 2 * index + 2

        smallest_index = index

        if index_left < len(self.heap) and self.heap[index_left] < self.heap[index]:
            smallest_index = index_left

        if (
            index_right < len(self.heap)
            and self.heap[index_right] < self.heap[smallest_index]
        ):
            smallest_index = index_right

        if index != smallest_index:
            self.heap[index], self.heap[smallest_index] = (
                self.heap[smallest_index],
                self.heap[index],
            )
            self.fix_down(smallest_index)
        # your implementation here


if __name__ == "__main__":
    n = [210, 100, 23, 2, 5]
    heap_transform = HeapTransformer(n)
    heap_transform.transform()
    print(heap_transform.heap)
