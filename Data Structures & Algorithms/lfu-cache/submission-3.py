class LFUCache:

    def __init__(self, capacity):
        self.cap = capacity
        self.val = {}
        self.freq = {}
        self.buckets = defaultdict(OrderedDict)
        self.min_freq = 0
    
    def _bump(self, key):
        frequency = self.freq[key]
        del self.buckets[frequency][key]
        if not self.buckets[frequency]:
            del self.buckets[frequency]
            if self.min_freq == frequency:
                self.min_freq +=1
        self.freq[key] = frequency + 1
        self.buckets.setdefault(frequency + 1, {})[key] = None
    
    def get(self, key):
        if key not in self.val:
            return -1
        self._bump(key)
        return self.val[key]
    
    def put(self, key, value):
        if self.cap <= 0:
            return
        if key in self.val:
            self.val[key] = value
            self._bump(key)
            return
        if len(self.val) >= self.cap:
            bucket = self.buckets[self.min_freq]
            evict = next(iter(bucket))
            del bucket[evict]
            if not bucket:
                del self.buckets[self.min_freq]
            del self.val[evict]
            del self.freq[evict]
        
        self.val[key] = value
        self.freq[key] = 1
        self.buckets.setdefault(1, {})[key] = None
        self.min_freq = 1


