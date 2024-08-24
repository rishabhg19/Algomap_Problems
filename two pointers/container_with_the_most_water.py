# Leetcode 11 Container with the most water
# Algomap Two Pointers
# Solution move pointer in when height at
# pointer is less, update area when area greater than currentå

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        currMax = min(height[left], height[right]) * (right - left)

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            currMax = max(currMax, min(height[left], height[right]) * (right - left))
        return currMax