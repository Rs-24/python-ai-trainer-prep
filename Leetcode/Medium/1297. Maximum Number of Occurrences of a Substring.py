

from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # Time: O(n)
        # Space: O(n)
        c = [0] * 26
        d = defaultdict(int)
        distinct = l = ans = 0
        for r in range(len(s)):
            i = ord(s[r]) - ord("a")
            c[i] += 1
            distinct += c[i] == 1
            if r - l + 1 > minSize:
                i = ord(s[l]) - ord("a")
                c[i] -= 1
                distinct -= c[i] == 0
                l += 1
            if r - l + 1 == minSize and distinct <= maxLetters:
                d[s[l:r + 1]] += 1
                ans = max(ans, d[s[l:r + 1]])
        return ans


