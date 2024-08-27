# Leetcode 167 Two Sum II - Input Array Is Sorted
# Algomap Two Pointers
# Solution - intuitive
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        result = []

        while left < right and numbers[left] + numbers[right] != target:
            if target - numbers[left] < numbers[right]:
                right -= 1
            elif target - numbers[left] > numbers[right]:
                left += 1
            else:
                result = [left+1, right+1]
        result = [left+1, right+1]
        return result
