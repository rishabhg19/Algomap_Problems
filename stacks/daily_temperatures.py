class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for index, value in enumerate(temperatures):
            if stack:
                while stack and stack[-1][1] < value:
                    result[stack[-1][0]] = index - stack[-1][0]
                    stack.pop()
            stack.append((index,value))
            
        #print(result)
        return result
        