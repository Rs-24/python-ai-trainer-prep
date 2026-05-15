

class Solution:
    def maxScore(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        zeros = 0
        ones = s.count("1")
        best = 0
        for i, ch in enumerate(s):
            if ch == "0":
                zeros += 1
            else:
                ones -= 1
            if i < len(s) - 1:
                best = max(best, zeros + ones)
        return best


