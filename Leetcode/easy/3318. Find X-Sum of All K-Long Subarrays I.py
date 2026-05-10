# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description/

from typing import List
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # Time: O((n - k) * k log k), n = len(nums)
        # Aux space: O(k) 
        def x_sum(arr: List[int]) -> int:
            c = Counter(arr)
            temp = list(c.items())
            temp.sort(key=lambda t: (-t[1], -t[0]))
            return sum(val * freq for val, freq in temp[:x])
        out = []
        for i in range(len(nums) - k + 1):
            out.append(x_sum(nums[i:i + k]))
        return out


