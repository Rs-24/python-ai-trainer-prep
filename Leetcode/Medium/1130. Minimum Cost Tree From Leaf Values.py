

class Solution:
    def mctFromLeafValues(self, arr: list) -> int:
        # Time: O(n)
        # Space: O(n)
        a, s = 0, []
        for x in arr:
            while s and s[-1] <= x:
                y = s.pop()
                a += y * min(s[-1], x) if s else y * x
            s.append(x)
        while len(s) > 1:
            a += s.pop() * s[-1]
        return a


