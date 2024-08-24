# Leetcode 977 Squares of a sorted array
# Algomap two pointers
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []
        while left <= right:
            if abs(nums[right]) < abs(nums[left]):
                square = nums[left]**2
                left += 1
            else:
                square = nums[right]**2
                right -= 1
            result.append(square)
        return reversed(result)
        