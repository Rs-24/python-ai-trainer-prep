

class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list]) -> int:
        # Time: O(n)
        # Space: O(1)
        b = [0, 0, 0]
        for l, w in dimensions:
            d2 = l ** 2 + w ** 2
            if d2 > b[2]:
                b = [l, w, d2]
            elif d2 == b[2] and l * w > b[0] * b[1]:
                b = [l, w, d2]
        return b[0] * b[1]


