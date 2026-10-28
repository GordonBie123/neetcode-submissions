class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            middle = (left + right) // 2
            hours_needed = sum((p + middle - 1) // middle for p in piles)

            if hours_needed <= h:
                ans = middle
                right = middle - 1
            else:
                left = middle + 1
        return ans


