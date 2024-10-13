class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = sum(nums[:k])
        left = 0
        result = currSum
        for right in range(k, len(nums)):
            currSum += nums[right] - nums[left]
            result = max(result, currSum)
            left += 1
        return result / k