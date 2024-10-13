class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currSum = 0
        results = []
        for right in range(len(nums)):
            currSum += nums[right]
            while currSum >= target:
                results.append(right - left + 1)
                currSum -= nums[left]
                left += 1
        return min(results) if results else 0
        