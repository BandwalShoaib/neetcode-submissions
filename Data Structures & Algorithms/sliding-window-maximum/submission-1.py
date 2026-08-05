class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res,tot = [],[]
        m = len(nums)

        for r in range(m-k+1):
           res.append(max(nums[r:r+k]))
        tot = res
        return tot