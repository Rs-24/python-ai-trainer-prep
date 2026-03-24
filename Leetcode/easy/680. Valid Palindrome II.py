# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(1)
        def ispalindrome(a: int, b: int) -> bool:
            while a < b:
                if s[a] != s[b]:
                    return False
                a += 1
                b -= 1
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return ispalindrome(l + 1, r) or ispalindrome(l, r - 1)
            l += 1
            r -= 1
        return True


