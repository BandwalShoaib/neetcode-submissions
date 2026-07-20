class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join([ch.lower() for ch in s if ch.isalnum()])
        left, right = 0, len(clean_text) - 1
        while left < right:
            if clean_text[left] != clean_text[right]:
                return False
            left += 1
            right -= 1
        return True
        