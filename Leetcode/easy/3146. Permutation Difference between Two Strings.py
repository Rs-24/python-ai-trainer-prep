# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/permutation-difference-between-two-strings/description/

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        # Time: O(m + n), m = len(s), n = len(s)
        # Space: O(m)
        d = {}
        for i, ch in enumerate(s):
            d[ch] = i
        total = 0
        for i, ch in enumerate(t):
            total += abs(d[ch] - i)
        return total


