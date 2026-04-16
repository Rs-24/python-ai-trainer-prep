# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/description/

from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # Time: O(n * k + n log n), n = len(nums)
        # Aux space: O(n)
        s = set()
        key_indices = [i for i, num in enumerate(nums) if num == key]
        for i in key_indices:
            for di in range(k + 1):
                if 0 <= i + di < len(nums):
                    s.add(i + di)
                if 0 <= i - di < len(nums):
                    s.add(i - di)
        s = list(s)
        s.sort()
        return s


