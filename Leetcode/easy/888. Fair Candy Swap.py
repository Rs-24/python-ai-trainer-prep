

class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        # Time: O(m + n), m = len(aliceSizes), n = len(bobSizes)
        # Space: O(m)
        diff = sum(aliceSizes) - sum(bobSizes)
        s = set(aliceSizes)
        for b in bobSizes:
            need = (diff + 2 * b) // 2
            if need in s:
                return [b, need]


