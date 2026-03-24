# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/longest-uncommon-subsequence-i/description/

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # Time: O(1)
        # Space: O(1)
        if a == b:
            return -1
        return max(len(a), len(b))


