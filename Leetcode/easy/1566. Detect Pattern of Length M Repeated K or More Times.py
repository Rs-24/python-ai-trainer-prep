# Time to write all of below including tests, explanation and time and aux
# and total space: 6 mins

# Problem: https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/description/

from typing import List

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        # Time: O((n - m * k + 1) * (m * k))
        # Space: O(m * k)
        for i in range(len(arr) - m * k + 1):
            if arr[i:i + m] * k == arr[i:i + m * k]:
                return True
        return False

# Alternative version:
from typing import List
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        # Time: O(n - m), n = len(arr)
        # Space: O(1)
        count = 0
        for i in range(len(arr) - m):
            if arr[i] == arr[i + m]:
                count += 1
                if count == m * (k - 1):
                    return True
            else:
                count = 0
        return False
            

