# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/split-a-string-in-balanced-strings/description/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        l_minus_r = 0
        total = 0
        for ch in s:
            l_minus_r += 1 if ch == "L" else -1
            total += 1 if l_minus_r == 0 else 0
        return total


