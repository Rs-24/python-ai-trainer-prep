

from collections import defaultdict

class Solution:
    def countKDifference(self, nums: list, k: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        count = 0
        d = defaultdict(int)
        for num in nums:
            count += d[num - k]
            count += d[num + k]
            d[num] += 1
        return count


