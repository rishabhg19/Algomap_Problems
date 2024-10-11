class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            y = stones[-1]
            x = stones[-2]
            if y != x:
                temp = y - x
                stones.pop()
                stones[-1] = temp
            else:
                stones.pop()
                stones.pop()
            stones.sort()
        return stones[0] if stones else 0
        