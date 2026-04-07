# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/

from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        # Time: O(n), n = len(arr)
        # Space: O(1)
        if sum(arr) % 3 != 0:
            return False
        expected = sum(arr) // 3
        total = 0
        parts_found = 0
        for num in arr:
            total += num
            if total == expected:
                total = 0
                parts_found += 1
        return parts_found >= 3


