

class Solution:
    def findBestValue(self, arr: list, target: int) -> int:
        # Time: O(n log max(arr))
        # Space: O(1)
        def s(x: int) -> int:
            return sum(min(num, x) for num in arr)
        l, r = 0, max(arr)
        while l < r:
            m = (l + r) // 2
            if s(m) < target:
                l = m + 1
            else:
                r = m
        if l == 0:
            return 0
        return l - 1 if abs(s(l - 1) - target) <= abs(s(l) - target) else l


