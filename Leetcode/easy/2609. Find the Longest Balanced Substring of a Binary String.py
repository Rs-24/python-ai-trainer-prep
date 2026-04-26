# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/description/

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        best = 0
        zeroes = 0
        ones = 0
        prev = None
        for i, ch in enumerate(s):
            if ch == "0":
                if prev == "1":
                    zeroes = 1
                    ones = 0
                else:
                    zeroes += 1
            elif ch == "1":
                ones += 1
                best = max(best, 2 * min(zeroes, ones))
            prev = ch
        return best


