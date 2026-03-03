# Time to write all of below including tests, explanation and time and aux
# and total space: 25 mins

# Problem: https://leetcode.com/problems/longest-palindromic-substring/description/

from typing import Tuple
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l: int, r: int) -> Tuple[int, int]:
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1
        best_l = best_r = 0
        for i in range(len(s)):
            l1, r1 = expand(i, i)
            if i + 1 < len(s):
                l2, r2 = expand(i, i + 1)
            else:
                l2 = r2 = 0
            if r1 - l1 > best_r - best_l:
                best_l, best_r = l1, r1
            if r2 - l2 > best_r - best_l:
                best_l, best_r = l2, r2
        return s[best_l:best_r+1]

if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPalindrome("a") == "a"
    assert sol.longestPalindrome("A") == "A"
    assert sol.longestPalindrome("1") == "1"
    assert sol.longestPalindrome("aA") in ("a", "A")
    assert sol.longestPalindrome("a1a") == "a1a"
    assert sol.longestPalindrome("aAb1") in ("a", "A", "b", "1")
    assert sol.longestPalindrome("1111") == "1111"
    assert sol.longestPalindrome("1234") in ("1", "2", "3", "4")
  
# Explanation: the code expands every index and double index to find the
# longest palindrome
# Time: O(n^2), n = len(s)
# Space: excluding output: O(1)

# dynamic programming method:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time: O(n^2), n = len(s)
        # Space: excluding output: O(n^2)
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        best_l = best_r = 0
        for length in range(1, n + 1):
            for l in range(n):
                r = length + l - 1
                if not (0 <= l < n):
                    continue
                if not (0 <= r < n):
                    continue
                if l > r:
                    continue
                if s[l] == s[r]:
                    if length <= 3:
                        dp[l][r] = True
                    if l + 1 <= r - 1 and 0 <= l + 1 < n and 0 <= r - 1 < n:
                        if dp[l + 1][r - 1] == True:
                            dp[l][r] = True
                    if dp[l][r] == True:
                        if length > best_r - best_l + 1:
                            best_l, best_r = l, r
        return s[best_l:best_r + 1]


