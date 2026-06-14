

from collections import Counter

class Solution:
    def firstUniqueEven(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        c = Counter(nums)
        for n in nums:
            if n % 2 == 0 and c[n] == 1:
                return n
        return -1


