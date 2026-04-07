# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/remove-palindromic-subsequences/description/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(n)
        return 1 if s == s[::-1] else 2


