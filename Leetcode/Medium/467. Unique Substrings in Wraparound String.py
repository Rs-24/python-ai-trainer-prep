

class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        dp = [0] * 26
        c = 0
        for i, ch in enumerate(s):
            if i > 0:
                if (ord(ch) - ord(s[i - 1])) % 26 == 1:
                    c += 1
                else:
                    c = 1
            else:
                c = 1
            dp[ord(ch) - ord("a")] = max(dp[ord(ch) - ord("a")], c)
        return sum(dp)


