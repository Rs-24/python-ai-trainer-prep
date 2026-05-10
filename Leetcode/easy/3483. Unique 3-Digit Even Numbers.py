# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/unique-3-digit-even-numbers/description/

from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # Time: O(n^3), n = len(digits)
        # Space: O(n)
        n = len(digits)
        seen = set()
        for i in range(n):
            if digits[i] % 2 != 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if digits[k] == 0:
                        continue
                    seen.add(digits[k] * 100 + digits[j] * 10 + digits[i])
        return len(seen)


