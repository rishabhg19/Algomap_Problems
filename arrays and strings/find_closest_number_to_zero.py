# Leetcode 2239 Find Closest Number to Zero
# Algomap Arrays and Strings 1

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for num in nums[1:]:
            if abs(num) < abs(closest):
                closest = num
            elif abs(num) == abs(closest):
                closest = max(num, closest)
        return closest
        