

from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        # Time: O(m log m + n), m = len(arr1), n = len(arr2)
        # Space: O(m + n)
        out = []
        c = Counter(arr1)
        for num in arr2:
            out.extend([num] * c[num])
            del c[num]
        for num, freq in sorted(c.items()):
            out.extend([num] * c[num])
        return out


