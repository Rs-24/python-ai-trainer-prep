

from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: list) -> list:
        # Time: O(n)
        # Space: O(n)
        return [n for n, f in Counter(nums).items() if f == 2]


