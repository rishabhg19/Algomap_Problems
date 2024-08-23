# Leetcode 771 Stones and jewels
# Algomap hashmaps and sets
# solution is just checking membership

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelset = set()
        for jewel in jewels:
            jewelset.add(jewel)
        count = 0
        for stone in stones:
            if stone in jewelset:
                count += 1
        return count
        