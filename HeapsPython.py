import heapq

# It is the min heap implementation in python

nums = [4, 7, 4, -2, 1, 0]

# heapq.heapify(nums)
#
# print(nums)


heap = []

for value in nums:
    heapq.heappush(heap, value)

print(heap)

while heap:
    print(heapq.heappop(heap))
