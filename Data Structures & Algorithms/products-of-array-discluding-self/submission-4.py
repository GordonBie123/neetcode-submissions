class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        # Prefix
        for i, n in enumerate(nums):
            res[i] *= prefix
            prefix *= n

        suffix = 1
        # Suffix
        for i in range(len(nums) -1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i] 
        
        return res

        