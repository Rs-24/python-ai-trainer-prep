# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/

from typing import List
from collections import defaultdict

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        count = 0
        freq = defaultdict(int)
        for num in nums:
            count += freq[num - k]
            count += freq[num + k]
            freq[num] += 1
        return count


