
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if str(n) not in count:
                count[str(n)] = 1
            elif str(n) in count:
                count[str(n)] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []
        for i in range((len(buckets) - 1), 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

            