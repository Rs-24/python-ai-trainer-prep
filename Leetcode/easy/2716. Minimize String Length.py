# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimize-string-length/description/

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        return len(set(s))


