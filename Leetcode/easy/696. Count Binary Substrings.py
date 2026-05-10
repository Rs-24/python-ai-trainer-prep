

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        prev = 0
        cur = 1
        count = 0
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                cur += 1
            else:
                count += min(cur, prev)
                prev = cur
                cur = 1
        count += min(cur, prev)
        return count


