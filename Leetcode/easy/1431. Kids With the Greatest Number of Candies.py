

class Solution:
    def kidsWithCandies(self, candies: list, extraCandies: int) -> list:
        # Time: O(n), n = len(candies)
        # Space: O(n)
        out = []
        best = max(candies)
        for c in candies:
            if c + extraCandies >= best:
                out.append(True)
            else:
                out.append(False)
        return out


