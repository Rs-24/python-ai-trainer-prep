# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-distinct-difference-array/description/

from typing import List

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Aux space: O(n)
        out = []
        before = set()
        after = set(nums)
        for num in nums:
            before.add(num)
            after.remove(num)
            out.append(len(before) - len(after))
        return out


