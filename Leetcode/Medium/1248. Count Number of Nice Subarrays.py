

from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: list, k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        ans = 0
        for num in nums:
            prefix += num % 2
            ans += count[prefix - k]
            count[prefix] += 1
        return ans


