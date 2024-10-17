class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0,1,2]
        for stair in range(3,n+1):
            memo.append(memo[stair-1]+memo[stair-2])
        return memo[n]
        