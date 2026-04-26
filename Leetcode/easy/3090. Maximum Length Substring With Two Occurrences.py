# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        count = [0] * 26
        l = 0
        best = 0
        for r, ch in enumerate(s):
            idx = ord(ch) - ord("a")
            count[idx] += 1
            while count[idx] > 2:
                count[ord(s[l]) - ord("a")] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best


