class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqs = Counter(nums)
        for num in freqs:
            if freqs[num] > len(nums) // 2:
                return num