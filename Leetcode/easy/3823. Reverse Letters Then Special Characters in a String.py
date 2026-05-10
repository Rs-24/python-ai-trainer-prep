# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/description/

class Solution:
    def reverseByType(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalpha():
                l += 1
            while l < r and not s[r].isalpha():
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and s[l].isalpha():
                l += 1
            while l < r and s[r].isalpha():
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)


