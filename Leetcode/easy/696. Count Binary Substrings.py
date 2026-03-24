# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/count-binary-substrings/description/

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        prev = 0
        cur = 1
        total = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                total += min(cur, prev)
                prev = cur
                cur = 1
        total += min(cur, prev)
        return total


