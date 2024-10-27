class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        left = 0
        currSum = 0
        maxi = 0
        for right in range(len(nums)):
            print(left, right, maxi)
            currSum += nums[right]
            while currSum < 0:
                currSum -= nums[left]
                left += 1
            maxi = max(currSum, maxi)
        return maxi

        