from collections import defaultdict,Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result =[]
        for word,count in count.most_common(k):
            result.append(word)
        return result
        