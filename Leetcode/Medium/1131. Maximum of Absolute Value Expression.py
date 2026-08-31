

class Solution:
    def maxAbsValExpr(self, arr1: list, arr2: list) -> int:
        # Time: O(n)
        # Space: O(1)
        a = 0
        for d1, d2 in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            mi, ma = float("inf"), float("-inf")
            for i in range(len(arr1)):
                t = d1 * arr1[i] + d2 * arr2[i] + i
                mi = min(mi, t)
                ma = max(ma, t)
            a = max(a, ma - mi)
        return a


