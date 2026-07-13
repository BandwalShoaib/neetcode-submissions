from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visited = defaultdict(int)
        for i in s:
            visited[i] += 1
        for i in t:
            visited[i] -= 1
        is_anagram = True
        for i,j in visited.items():
            if j != 0:
                is_anagram = False
                break
        return is_anagram
