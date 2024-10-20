class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freqs = Counter()
        left = 0
        longest = 0
        if len(s) <= 1:
            return len(s)
        for right in range(len(s)):
            freqs[s[right]] += 1
            longest = max(longest, len(freqs))
            while max(freqs.values()) > 1:
                if freqs[s[left]] > 1:
                    freqs[s[left]] -= 1
                else:
                    del freqs[s[left]]
                left += 1
        return longest
        