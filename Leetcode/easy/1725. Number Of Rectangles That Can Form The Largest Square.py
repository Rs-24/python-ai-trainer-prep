

class Solution:
    def countGoodRectangles(self, rectangles: list[list]) -> int:
        # Time: O(n), n = len(rectangles)
        # Space: O(1)
        best = c = 0
        for l, w in rectangles:
            a = min(l, w) * min(l, w)
            if a > best:
                best = a
                c = 1
            elif a == best:
                c += 1
        return c


