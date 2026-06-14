

from collections import Counter

class Solution:
    def duplicateNumbersXOR(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        c = Counter(nums)
        t = 0
        for n, f in c.items():
            if f == 2:
                t ^= n
        return t


