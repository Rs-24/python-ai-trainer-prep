# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/

from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Time: O(n log n), n = len(nums)
        # Aux space: O(n)
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort(key = lambda x: x[0], reverse = True)
        arr = arr[:k]
        arr.sort(key = lambda x: x[1])
        return [num for num, _ in arr]


