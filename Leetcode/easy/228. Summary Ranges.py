# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/summary-ranges/description/

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Time: O(n), n = len(nums)
        # Space, excluding output: O(1)
        if not nums:
            return []
        out = []
        start = nums[0]
        prev = nums[0]
        for num in nums[1:]:
            if num - prev > 1:
                if start == prev:
                    out.append(str(prev))
                else:
                    out.append((str(start) + "->" + str(prev)))
                start = num
            prev = num
        if start == prev:
            out.append(str(prev))
        else:
            out.append((str(start) + "->" + str(prev)))
        return out


