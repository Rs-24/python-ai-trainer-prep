

class Solution:
    def mergeSimilarItems(self, items1: list[list], items2: list[list]) -> list[list]:








        d = {}
        for a, b in items1:
            d[a] = d.get(a, 0) + b
        for a, b in items2:
            d[a] = d.get(a, 0) + b
        return [[num, d[num]] for num in sorted(d)]


