class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for n, freq in counter.items():
            buckets[freq].append(n)

        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for item in buckets[freq]:
                res.append(item)

        return res[:k]

