class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Optimal approach is to use a bucket sort.
        # Create list of lists which serve as buckets and use a hash map counter to find the freq of each value 
        # The index in the buckets is the freq of a value 

        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        res = []
        for n, freq in counter.items():
            buckets[freq].append(n)
        
        for freq in range(len(buckets) - 1, 0, -1):
            for value in buckets[freq]:
                res.append(value)

                if len(res) == k:
                    return res

        