

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        t = o = 0
        for ch in s:
            if ch == "1":
                o += 1
            else:
                t = min(t + 1, o)
        return t


        