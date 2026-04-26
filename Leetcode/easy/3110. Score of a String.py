# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/score-of-a-string/description/

class Solution:
    def scoreOfString(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        total = 0
        prev = ord(s[0])
        for ch in s:
            total += abs(ord(ch) - prev)
            prev = ord(ch)
        return total


