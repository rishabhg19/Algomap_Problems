from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        desired_freqs = [0] * 26
        for char in s1:
            desired_freqs[ord(char)-ord('a')] += 1
        freqs = [0] * 26
        left = 0
        for right in range(len(s2)):
            freqs[ord(s2[right])-ord('a')] += 1
            if right - left + 1 >= len(s1):
                if desired_freqs == freqs:
                    return True
                else:
                    freqs[ord(s2[left])-ord('a')] -= 1
                left += 1
        return False
        