# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/check-if-array-is-good/description/

from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        n = len(nums)
        seen = set()
        largest_val_count = 0
        for num in nums:
            if num < 1 or num > n - 1:
                return False
            if num == n - 1:
                largest_val_count += 1
            else:
                if num in seen:
                    return False
                seen.add(num)
        return largest_val_count == 2 and len(seen) == n - 2


