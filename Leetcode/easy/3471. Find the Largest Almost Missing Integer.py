# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-largest-almost-missing-integer/description/

from typing import List
from collections import defaultdict

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # Time: O(n * k), n = len(nums)
        # Space: O(k)
        n = len(nums)
        count = defaultdict(int)
        for i in range(n - k + 1):
            window = set(nums[i:i + k])
            for x in window:
                count[x] += 1
        best = -1
        for num, freq in count.items():
            if freq == 1:
                best = max(best, num)
        return best


