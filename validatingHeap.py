def is_min_heap(heap):
    # trivial case
    if len(heap) <= 1:
        return True

    if len(heap) == 2:
        return heap[0] < heap[1]

    # Total num of items that we need to consider in the array
    # for validating if its a min heap: r = 2*i +2 => i =
    num_items = (len(heap) - 2) // 2 + 1

    for i in range(num_items):
        # we have to check the heap property
        # the parent must be smaller than the children(min heap)
        if heap[i] > heap[2 * i + 1] or heap[i] > heap[2 * i + 2]:
            return False

    return True


def is_max_heap(heap):
    # trivial case
    if len(heap) <= 1:
        return True

    if len(heap) == 2:
        return heap[0] > heap[1]

    # Total num of items that we need to consider in the array
    # for validating if its a min heap: r = 2*i +2 => i =
    num_items = (len(heap) - 2) // 2 + 1

    for i in range(num_items):
        # we have to check the heap property
        # the parent must be smaller than the children(min heap)
        if heap[i] < heap[2 * i + 1] or heap[i] < heap[2 * i + 2]:
            return False

    return True


if __name__ == "__main__":
    n = [1, 2, 3, 5, 4]

    print(is_min_heap(n))

    n = [1, 2, 3, 5, -4]

    print(is_min_heap(n))

    n = [210, 100, 2, 5, 23]

    print(is_max_heap(n))
