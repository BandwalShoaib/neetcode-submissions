class Solution:
    def encode(self, strs: list[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        return s

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":   # find separator
                j += 1
            length = int(s[i:j]) # extract length
            word = s[j+1 : j+1+length]
            res.append(word)
            i = j + 1 + length   # move pointer forward
        return res
