class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        setted = set(nums)
        possible = []

        for n in range(1, len(nums) + 1):
            if n not in setted:
                possible.append(n)
                
        return possible