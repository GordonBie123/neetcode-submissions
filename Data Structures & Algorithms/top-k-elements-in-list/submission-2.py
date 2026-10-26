class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for n, freq in counter.items():
            buckets[freq].append(n)
        
        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for n in buckets[freq]:
                result.append(n)
            
            if len(result) == k:
                return result