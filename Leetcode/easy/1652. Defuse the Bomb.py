# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/defuse-the-bomb/description/

from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # Time: O(n * abs(k))
        # Space, excluding output: O(1)
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        for i in range(n):
            j = 1 if k > 0 else -1
            total = 0
            while abs(j) <= abs(k):
                temp = i + j
                while temp < 0:
                    temp += n
                idx = temp % n
                total += code[idx]
                j += 1 if k > 0 else -1
            res[i] = total
        return res


