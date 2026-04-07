# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/mean-of-array-after-removing-some-elements/description/

from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        # Time: O(n log n), n = len(arr)
        # Space: O(n)
        arr.sort()
        n = len(arr)
        arr = arr[int(n * 0.05):int(0.95 * n)]
        return sum(arr) / len(arr)


