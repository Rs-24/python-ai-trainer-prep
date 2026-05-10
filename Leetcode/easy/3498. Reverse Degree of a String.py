# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/reverse-degree-of-a-string/description/

class Solution:
    def reverseDegree(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        ans = 0
        for i, ch in enumerate(s):
            ans += (i + 1) * (26 - ord(ch) + ord("a"))
        return ans


