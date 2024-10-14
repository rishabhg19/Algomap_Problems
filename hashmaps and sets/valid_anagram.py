class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sfreqs = [0] * 26
        tfreqs = [0] * 26
        for char in s:
            sfreqs[ord(char)-ord('a')] += 1
        for char in t:
            tfreqs[ord(char)-ord('a')] += 1
        return sfreqs == tfreqs
        