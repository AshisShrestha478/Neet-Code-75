class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right = 0,len(heights)-1
        maximum = 0

        while left < right:
            breadth = right - left
            if heights[left] > heights[right]:
                length = heights[right]
                right -= 1
            else:
                length = heights[left]
                left += 1
            maximum = max(maximum, (length*breadth))

        return maximum