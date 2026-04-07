# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

class Solution:
    def maxDepth(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        cur = 0
        best = 0
        for ch in s:
            if ch == "(":
                cur += 1
                best = max(best, cur)
            elif ch == ")":
                cur -= 1
        return best


