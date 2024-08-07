# Leetcode 14 Longest Common Prefix
# Algomap Arrays and Strings 6
# Idea - build the prefix character by character (checkchars())
# break out of building the prefix when the current character
# is not contained in the prefix of each string in the input list
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def checkchars(strs: List[str], i):
            same = False
            check = strs[0][i]
            count = 0
            for k in range(1,len(strs)):
                if strs[k][i] == check:
                    count += 1
            if count == len(strs) - 1:
                same = True
            if same:
                return check
            else:
                return ''
        lengths = [len(s) for s in strs]
        length = min(lengths)
        result = ""
        for i in range(length):
            currchar = checkchars(strs, i)
            if currchar == '':
                break
            result += currchar
        return result
        