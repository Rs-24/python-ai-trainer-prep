# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/

from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Time: O(m log m + m * n), m = len(nums), n = len(queries)
        # Aux space: O(m)
        nums.sort()
        out = []
        for q in queries:
            total = 0
            length = 0
            for i, num in enumerate(nums):
                total += num
                if total > q:
                    length = i
                    break
                elif i == len(nums) - 1:
                    length = i + 1
            out.append(length)
        return out


