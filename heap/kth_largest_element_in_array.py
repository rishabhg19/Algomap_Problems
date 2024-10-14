class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return
        newnums = [-1*num for num in nums]
        heapq.heapify(newnums)
        res = 0
        for i in range(k):
            num = heapq.heappop(newnums)
            res = -1*num
        return res