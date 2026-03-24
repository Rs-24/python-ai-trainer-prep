# Time to write all of below including tests, explanation and time and aux
# and total space: 11 mins

# Problem: https://leetcode.com/problems/repeated-substring-pattern/description/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Time: O(n^2), n = len(s)
        # Space: O(n)
        n = len(s)
        for r in range(n // 2):
            if n % (r + 1) == 0:
                window = s[0:r + 1]
                if window * (n // (r + 1)) == s:
                    return True
        return False

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(n)
        return s in (s + s)[1:-1]


