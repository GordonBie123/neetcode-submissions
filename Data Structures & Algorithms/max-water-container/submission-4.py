class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            height = min(heights[left], heights[right])
            length = right - left
            curr_area = height * length
            if curr_area >= max_area:
                max_area = curr_area
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
        