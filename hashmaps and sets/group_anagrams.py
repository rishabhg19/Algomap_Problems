# Leetcode 49 Group Anagrams
# Algomap Hashmaps and sets

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ord(character) - ord('a') gets the position of 
        # a character in the alphabet relative to 'a' so 25 for 'z'
        print(ord('z')-ord('a'))
        print((0,)*26)
        groups = defaultdict(list)
        for word in strs:
            freqs = [0]*26
            for character in word:
                freqs[ord(character)-ord('a')] += 1
            groups[tuple(freqs)].append(word)
        result = []
        for key in groups:
            result.append(groups[key])
        return result