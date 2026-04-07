# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/decompress-run-length-encoded-list/description/

from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        # Time: O(k), k = length of output
        # Space, excluding output: O(1)
        out = []
        for i in range(0, len(nums) - 1, 2):
            out.extend([nums[i + 1]] * nums[i])
        return out


