class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        def findSum(index, currSum, goal):
            if currSum == target and index < len(candidates):
                if sol[:] not in res:
                    res.append(sol[:])
                return
            goal = target - currSum
            if goal < 0:
                return
            else:
                if index < len(candidates):
                    sol.append(candidates[index])
                    findSum(index, currSum + candidates[index], goal)
                    sol.pop()
                    findSum(index + 1, currSum, goal)
        findSum(0, 0, target)
        return res

        