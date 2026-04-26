# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        return sum(min(num % 3, 3 - num % 3) for num in nums)


