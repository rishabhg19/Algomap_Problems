class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []
        nums = range(1,n+1)
        def backtrack(index):
            if len(sol) == k:
                res.append(sol[:])
                return
            for j in range(index, len(nums)):
                if sol:
                    if nums[j] not in sol and nums[j] > max(sol):
                        sol.append(nums[j])
                        backtrack(index+1)
                        sol.remove(nums[j])
                else:
                    sol.append(nums[j])
                    backtrack(index+1)
                    sol.remove(nums[j])
        backtrack(0)
        return res
        