from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for i in strs:
            key = ' '.join(sorted(i))
            count[key].append(i)
        return list(count.values())
        