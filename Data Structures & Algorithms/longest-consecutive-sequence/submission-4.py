class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort=[]
        sort = sorted(set(nums))
        total = 1
        current = 1
        if not nums:
            return 0
        else:
          for i in range(len(sort)):
            if sort[i] == sort[i-1]+1:
                current+=1
                total =max(total,current)
            else:
                current = 1
          return total
        