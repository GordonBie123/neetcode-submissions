class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr = 0
        res = []
        while curr < len(nums):
            left = curr - 1
            right = curr + 1
            left_product = 1
            right_product = 1
            while left >= 0:
                
                left_product *= nums[left] 
                left -=1
            while right < len(nums):
                
                right_product *= nums[right]
                right += 1
            res.append(left_product * right_product)
            curr += 1
        return res
            
                