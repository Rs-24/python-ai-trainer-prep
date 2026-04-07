# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/decode-xored-array/description/

from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # Time: O(n), n = len(encoded)
        # Space, excluding output: O(1)
        res = [first]
        for num in encoded:
            first ^= num
            res.append(first)
        return res


