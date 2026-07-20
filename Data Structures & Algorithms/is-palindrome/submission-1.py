class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = " ".join([char for char in s.lower() if char.isalnum()])
        rev = clean_text[::-1]
        if (clean_text == rev):
            return True
        else:
            return False
        