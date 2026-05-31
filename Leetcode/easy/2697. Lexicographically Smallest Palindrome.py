

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        # Time: O(n)
        # Spac: O(n)
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            s[l] = s[r] = min(s[l], s[r])
            l += 1
            r -= 1
        return "".join(s)


