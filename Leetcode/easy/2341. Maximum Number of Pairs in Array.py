

from collections import Counter

class Solution:
    def numberOfPairs(self, nums: list) -> list:
        # Time: O(n)
        # Space: O(n)
        c = Counter(nums)
        return [sum(freq // 2 for freq in c.values()), sum(freq % 2 for freq in c.values())]


