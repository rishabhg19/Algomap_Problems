class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        potentials = range(1,num)
        left = 1
        right = len(potentials)
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return False if num != 1 else True
        