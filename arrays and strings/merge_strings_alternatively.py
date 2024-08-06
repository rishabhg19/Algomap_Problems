# Leetcode 1768 Merge Strings Alternatively
# Algomap Arrays and Strings 2

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        length = max(len(word1), len(word2))
        for i in range(length):
            if i < len(word1) and i < len(word2):
                merged += word1[i] + word2[i]
            elif i < len(word1) and i >= len(word2):
                merged += word1[i]
            elif i >= len(word1) and i < len(word2):
                merged += word2[i]
        return merged