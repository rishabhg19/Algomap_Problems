# Leetcode 238 Product of Array Except Self
# Algomap Arrays and Strings 7
# Solution - get prefixes in an array (product of everything before)
# and suffixes product of everything after and multiply
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        for i in range(1,len(nums)):
            prefixes[i] = prod * nums[i-1]
            prod = prod * nums[i-1]
        prod = 1
        for i in reversed(range(len(nums))):
            suffixes[i] = prod
            prod = prod*nums[i]
        print(prefixes, suffixes)
        return [prefix * suffix for prefix, suffix in zip(prefixes, suffixes)]