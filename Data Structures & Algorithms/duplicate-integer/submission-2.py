class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        i = 0
        for n in nums:
            if n in seen:
                return True
            seen[n] = i
            i += 1
        return False