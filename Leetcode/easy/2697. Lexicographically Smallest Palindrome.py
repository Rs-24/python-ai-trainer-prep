# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/lexicographically-smallest-palindrome/description/

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Aux space: O(n)
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            best = min(s[l], s[r])
            s[l] = s[r] = best
            l += 1
            r -= 1
        return "".join(s)


