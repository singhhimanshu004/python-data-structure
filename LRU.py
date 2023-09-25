class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache_dict = dict()
        self.count = dict()
        self.cache = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.cache_dict.get(key):
            self.cache.remove(key)
            self.cache.append(key)
            self.count[key] = self.count[key] + 1
            return self.cache_dict.get(key)
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.cache_dict.get(key):
            # re-order
            self.cache.remove(key)
            self.cache.append(key)

            self.cache_dict[key] = value
            self.count[key] = self.count[key] + 1
        if len(self.cache) < self.capacity:
            self.cache.append(key)
            self.cache_dict[key] = value
            self.count[key] = 1
        else:
            sorted_count_dict = dict(
                sorted(self.count.items(), key=lambda item: item[1])
            )
            if (
                not list(sorted_count_dict.values())[0]
                == list(sorted_count_dict.values())[1]
            ):
                self.cache.remove(list(sorted_count_dict.keys())[0])
                del self.count[list(sorted_count_dict.keys())[0]]
                del self.cache_dict[list(sorted_count_dict.keys())[0]]

            else:
                popped_key = self.cache.pop(0)
                del self.count[popped_key]
                del self.cache_dict[popped_key]

            self.cache.append(key)
            self.cache_dict[key] = value
            self.count[key] = 1

            # 1. look in the count map for the key with the least counter, we insert on the first value - and then do
            # right shift until we reach the key to be evicted 2. insert the value on the first entry in cache - and
            # the rest would right shift


if __name__ == "__main__":
    capacity = 2
    obj = LFUCache(capacity)
    param_1 = obj.get(3)
    print(param_1)
    obj.put(3, 4)
    param_1 = obj.get(3)
    print(param_1)
    print(f"cache dict : {obj.cache_dict}")
    print(f"cache: {obj.cache}")
    print(f"cache count: {obj.count}")

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
