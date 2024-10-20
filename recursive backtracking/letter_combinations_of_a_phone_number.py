class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {'2' :['a','b','c'], '3': ['d','e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r','s'], '8':['t', 'u','v'], '9':['w','x','y','z']}
        res, sol = [], []
        def backtrack(index):
            if len(sol) == len(digits) or index >= len(digits):
                res.append(sol[:])
                return res
            for i in range(len(letters[digits[index]])):
                sol.append(letters[digits[index]][i])
                backtrack(index+1)
                sol.pop()
        backtrack(0)
        answer = [''.join(string) for string in res]
        return answer if answer != [""] else []