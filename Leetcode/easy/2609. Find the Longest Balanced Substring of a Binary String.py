

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        best = ones = zeros = 0
        for i, ch in enumerate(s):
            if ch == "0":
                if i > 0 and s[i - 1] == "1":
                    zeros = 1
                    ones = 0
                else:
                    zeros += 1
            elif ch == "1":
                ones += 1
                best = max(best, 2 * min(ones, zeros))
        return best


