

class Solution:
    def firstPalindrome(self, words: list) -> str:
        # Time: O(n), n = total number of characters in words
        # Space: O(1)
        def is_palindrome(s: str) -> bool:
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        for word in words:
            if is_palindrome(word):
                return word
        return ""


