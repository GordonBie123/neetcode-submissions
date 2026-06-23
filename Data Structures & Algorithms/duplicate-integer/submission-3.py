class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i, number in enumerate(nums):
            if number in seen:
                return True
            seen[number] = i
        return False