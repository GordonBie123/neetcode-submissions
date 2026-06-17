
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if str(n) not in count:
                count[str(n)] = 1
            elif str(n) in count:
                count[str(n)] += 1
        top_k = sorted(count, key=count.get, reverse=True)[:k]
        return top_k
            