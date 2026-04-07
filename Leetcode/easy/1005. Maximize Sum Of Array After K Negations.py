# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/

from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # Time: O(n log n), n = len(nums)
        # Space: O(n)
        nums.sort()
        i = 0
        while i < len(nums) and nums[i] < 0 and k > 0:
            nums[i] *= -1
            k -= 1
            i += 1
        return sum(nums) if k % 2 == 0 else sum(nums) - 2 * min(nums)

# Heap version:
from typing import List
import heapq
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # Time: O(n + k log n), n = len(nums)
        # Space: O(1)
        heapq.heapify(nums)
        for _ in range(k):
            num = heapq.heappop(nums)
            heapq.heappush(nums, -num)
        return sum(nums)


