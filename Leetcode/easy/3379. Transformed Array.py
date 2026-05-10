# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/transformed-array/description/

from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        result = []
        n = len(nums)
        for i in range(n):
            idx = i
            if nums[i] > 0:
                idx = (i + nums[i]) % n
            elif nums[i] < 0:
                idx = (i - abs(nums[i]))
                while idx < 0:
                    idx += n
                idx %= n
            result.append(nums[idx])
        return result


