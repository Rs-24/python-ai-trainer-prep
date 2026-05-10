# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/largest-even-number/description/

class Solution:
    def largestEven(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        if not any(ch == "2" for ch in s):
            return ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == "2":
                break
            i -= 1
        return s[:i + 1]


