class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minimum = 10000
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[right]:
                mini = min(nums[left], nums[mid], nums[right])
                minimum = min(minimum, mini)
                left = mid + 1
            else:
                mini = min(nums[left], nums[mid], nums[right])
                minimum = min(minimum, mini)
                right = mid - 1
        return minimum
                
            