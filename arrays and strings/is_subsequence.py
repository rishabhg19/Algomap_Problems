# Leetcode 392 Is Subsequence
# Algomap Arrays and Strings 4
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        pointer = 0
        for i in range(len(t)):
            if pointer < len(s) and s[pointer] == t[i]:
                    pointer += 1
        return pointer == len(s)
        