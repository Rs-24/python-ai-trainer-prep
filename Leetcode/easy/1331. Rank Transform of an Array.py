

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # Time: O(n log n), n = len(arr)
        # Space: O(n)
        d = {}
        for i, num in enumerate(sorted(set(arr))):
            d[num] = i + 1
        return [d[num] for num in arr]


