class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        def backtrack(index):
            print(sol[:])
            if index == len(nums):
                # solutions are at the bottom of DFS search tree
                res.append(sol[:])
                return

            # do not choose number at current index
            backtrack(index+1)

            # choose number at current index, append, and remove after call
            sol.append(nums[index])
            backtrack(index+1)
            sol.pop()
        
        backtrack(0)
        return res
            