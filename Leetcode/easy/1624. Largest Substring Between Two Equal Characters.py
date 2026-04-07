# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        d = {}
        best = -1
        for i, ch in enumerate(s):
            if ch in d:
                best = max(best, i - d[ch] - 1)
            else:
                d[ch] = i
        return best


