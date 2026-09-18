class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.timekey = {}
        self.time = 0

    def get(self, key: int) -> int:
        res = self.cache.get(key)
        
        if res != None:
            self.timekey[key] = self.time
            self.time += 1
            return res
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity and key not in self.cache:
            # remove LRU
            min_time = min(self.timekey.values())
            for k in self.timekey:
                if self.timekey[k] == min_time:
                    min_key = k
                    break
            
            self.cache.pop(min_key, None)
            self.timekey.pop(min_key, None)
            self.cache[key] = value

        else:
            self.cache[key] = value

        self.timekey[key] = self.time
        self.time += 1
        
