# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/fair-candy-swap/description/

from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # Time: O(m + n), m = len(aliceSizes), n = len(bobSizes)
        # Space, excluding output: O(n)
        diff = sum(bobSizes) - sum(aliceSizes)
        b = set(bobSizes)
        for a in aliceSizes:
            needed = (diff + 2 * a) // 2
            if needed in b:
                return [a, needed]


