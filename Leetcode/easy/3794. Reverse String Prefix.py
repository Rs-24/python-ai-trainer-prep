# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/reverse-string-prefix/description/

class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        return s[:k][::-1] + s[k:]


