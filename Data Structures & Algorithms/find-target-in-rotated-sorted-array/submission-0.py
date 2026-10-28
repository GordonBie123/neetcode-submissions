class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right: 
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            
            # left portion
            if nums[middle] >= nums[left]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1   
            
            # [3,4,5,6,1,2]
            # [1,2,3,4,5,6]
            # [6,1,2,3,4,5] # t = 1
            # right portion
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1
                
                    
