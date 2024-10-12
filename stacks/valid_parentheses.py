class Solution:
    def isValid(self, s: str) -> bool:
        closes = {"}": "{", ")": "(", "]":"["}
        stack = []
        if len(s) % 2 == 1:
            return False
        for character in s:
            if character not in closes:
                stack.append(character)
            if character in closes:
                if stack:
                    if stack[-1] == closes[character]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return False if stack else True
        