

from collections import defaultdict

class Solution:
    def mostFrequent(self, nums: list, key: int) -> int:
        # Time: O(n)
        # Space: O(n)
        d = defaultdict(int)
        for i in range(len(nums) - 1):
            if nums[i] == key:
                d[nums[i + 1]] += 1
        best = max(d.values())
        for num, freq in d.items():
            if freq == best:
                return num


