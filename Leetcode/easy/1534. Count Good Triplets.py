# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/count-good-triplets/description/

from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # Time: O(n^3), n = len(arr)
        # Space: O(1)
        n = len(arr)
        total = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if abs(arr[i] - arr[j]) <= a:
                        if abs(arr[j] - arr[k]) <= b:
                            if abs(arr[i] - arr[k]) <= c:
                                total += 1
        return total


