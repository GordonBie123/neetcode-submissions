import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h -> how many hours we have to eat all the bananas
        # k -> Bananas per hour eating rate
        # piles[i]  the amount of bananas in pile i

        low, high = 1, max(piles)
        while low < high:
            k = (low + high) // 2
            hours = sum(-(-p // k) for p in piles)
            if hours <= h:
                high = k
            else:
                low = k + 1
        return low
