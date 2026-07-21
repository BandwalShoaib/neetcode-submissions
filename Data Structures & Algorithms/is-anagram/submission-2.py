from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      visited = defaultdict(int)
      for i in s:
        visited[i] += 1
      for i in t:
        visited[i] -= 1
      for value,freq in visited.items():
        if freq == 0:
            ans = True
        else:
            ans = False
      return ans
