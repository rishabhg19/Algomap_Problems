# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        versions = range(1,n+1)
        left = 1
        if isBadVersion(left):
            return left
        if isBadVersion(n) and n==2:
            return n
        right = n
        while isBadVersion(left) == False:
            mid = (right+left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left