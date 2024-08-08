# Leetcode 228 Summary Ranges
# Algomap Arrays and Strings 7
# Solution - obvious but hardcoded last iteration
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []
        start_index = 0
        end_index = 0
        ranges = []
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                end_index += 1
            else:
                if start_index != end_index:
                    ranges.append(str(nums[start_index])+"->"+str(nums[end_index]))
                else:
                    ranges.append(str(nums[start_index]))
                start_index = i
                end_index = i
        if start_index != end_index:
            ranges.append(str(nums[start_index])+"->"+str(nums[end_index]))
        else:
            ranges.append(str(nums[start_index]))
        return ranges
        