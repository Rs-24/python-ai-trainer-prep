# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/degree-of-an-array/description/

from typing import List 

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        first = {}
        last = {}
        freqs = {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            freqs[num] = freqs.get(num, 0) + 1
        max_freq = max(freqs.values())
        best = len(nums)
        for num, freq in freqs.items():
            if freq == max_freq:
                best = min(best, last[num] - first[num] + 1)
        return best


