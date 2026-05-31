

class Solution:
    def mergeSimilarItems(self, items1: list[list], items2: list[list]) -> list[list]:
        # Time: O(n log n)
        # Space: O(n)
        d = {}
        for a, b in items1:
            d[a] = d.get(a, 0) + b
        for a, b in items2:
            d[a] = d.get(a, 0) + b
        return [[v, d[v]] for v in sorted(d)]


