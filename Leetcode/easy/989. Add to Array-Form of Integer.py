# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/add-to-array-form-of-integer/description/

from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # Time: O(n + log k), n = len(num)
        # Space, excluding output: O(1)
        i = len(num) - 1
        result = []
        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
                i -= 1
            result.append(k % 10)
            k //= 10
        result.reverse()
        return result


