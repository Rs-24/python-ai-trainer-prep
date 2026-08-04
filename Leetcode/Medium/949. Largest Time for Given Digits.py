

from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: list) -> str:
        # Time: O(1)
        # Space: O(1)
        t = -1
        for a, b, c, d in permutations(arr):
            h, m = 10 * a + b, c * 10 + d
            if h < 24 and m < 60:
                t = max(t, h * 60 + m)
        if t == -1:
            return ""
        return f"{t // 60:02d}:{t % 60:02d}"


        