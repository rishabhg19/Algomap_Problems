class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freqs = Counter(nums)
        if max(freqs.values()) > 1:
            return True
        return False
        