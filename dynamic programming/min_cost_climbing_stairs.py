class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        costs = [0] + cost + [0]
        print(costs)
        n = len(costs) - 1
        memo = {1: costs[1], 2: min(costs[1]+costs[2], costs[2])}
        for step in range(3,n+1):
            memo[step] = min(memo[step-1] + costs[step], costs[step]+memo[step-2])
        #print(memo)
        return memo[n]

        