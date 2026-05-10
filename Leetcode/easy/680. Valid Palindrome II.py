

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(1)
        def is_palindrome(a: int, b: int) -> bool:
            while a < b:
                if s[a] != s[b]:
                    return False
                a += 1
                b -= 1
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
            l += 1
            r -= 1
        return True


