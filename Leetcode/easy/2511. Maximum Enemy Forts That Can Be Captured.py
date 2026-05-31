

class Solution:
    def captureForts(self, forts: list) -> int:
        # Time: O(n)
        # Space: O(1)
        last_minus = last_one = -1
        l = [None, -1]
        b = 0
        for i, ch in enumerate(forts):
            if abs(ch) == 1:
                if l[1] != -1 and l[0] != ch:
                    b = max(b, i - l[1] - 1)
                l = [ch, i]
        return b


