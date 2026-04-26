# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/separate-the-digits-in-an-array/description/

from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        # Time: O(d), d = total number of digits in nums
        # Space: O(d)
        def separate(x: int):
            out = [0] if x == 0 else []
            while x > 0:
                out.append(x % 10)
                x //= 10
            return reversed(out)
        res = []
        for num in nums:
            res.extend(separate(num))
        return res


