# Time to write all of below including tests, explanation and time and aux
# and total space: 6 mins

# Problem: https://leetcode.com/problems/squares-of-a-sorted-array/description/

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Space, excluding output: O(1)
        n = len(nums)
        out = [0] * n
        insert_pos = n - 1
        l, r = 0, n - 1
        while l <= r:
            l_square = nums[l] * nums[l]
            r_square = nums[r] * nums[r]
            if l_square > r_square:
                out[insert_pos] = l_square
                l += 1
            else:
                out[insert_pos] = r_square
                r -= 1
            insert_pos -= 1
        return out


