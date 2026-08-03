class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1),len(s2)
        l = 0

        for r in range(m-n+1):
            if sorted(s2[r:r+n]) == sorted(s1):
                return True
        return False
    
        