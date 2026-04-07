# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/check-if-n-and-its-double-exist/description/

from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Time: O(n)
        # Space: O(n)
        seen = set()
        for num in arr:
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False


