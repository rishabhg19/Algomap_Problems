class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [],[]

        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
        
            for j in range(len(nums)):
                if nums[j] not in sol:
                    sol.append(nums[j])
                    backtrack()
                    sol.remove(nums[j])

        backtrack()
        return res