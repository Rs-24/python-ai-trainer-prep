

from collections import defaultdict

class Solution:
    def largestInteger(self, nums: list, k: int) -> int:
        # Time: O(n^2)
        # Space: O(n)
        c = defaultdict(int)
        for i in range(len(nums) - k + 1):
            w = set(nums[i:i + k])
            for x in w:
                c[x] += 1
        b = -1
        for n, f in c.items():
            if f == 1:
                b = max(b, n)
        return b


