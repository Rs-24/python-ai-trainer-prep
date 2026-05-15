

class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        # Time: O(n), n = len(dominoes)
        # Space: O(n)
        d = {}
        count = 0
        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            count += d.get(key, 0)
            d[key] = d.get(key, 0) + 1
        return count


