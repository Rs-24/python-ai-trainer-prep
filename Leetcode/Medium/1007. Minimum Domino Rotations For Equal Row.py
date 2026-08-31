

class Solution:
    def minDominoRotations(self, tops: list, bottoms: list) -> int:
        # Time: O(n)
        # Space: O(1)
        def r(x: int) -> int:
            rt = rb = 0
            for t, b in zip(tops, bottoms):
                if t != x and b != x:
                    return float("inf")
                rt += t != x
                rb += b != x
            return min(rt, rb)
        a = min(r(tops[0]), r(bottoms[0]))
        return -1 if a == float("inf") else a


