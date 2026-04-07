# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/consecutive-characters/description/

class Solution:
    def maxPower(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        best = 1
        cur = 1
        prev = s[0]
        for ch in s[1:]:
            if ch == prev:
                cur += 1
            else:
                cur = 1
            best = max(best, cur)
            prev = ch
        return best


