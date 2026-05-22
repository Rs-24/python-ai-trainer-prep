

from collections import Counter

class Solution:
    def divideArray(self, nums: list) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        c = Counter(nums)
        return all(freq % 2 == 0 for freq in c.values())


