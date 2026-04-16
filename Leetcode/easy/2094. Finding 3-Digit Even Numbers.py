# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/finding-3-digit-even-numbers/description/

from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # Time: O(n), n = len(digits)
        # Aux space: O(1)
        out = []
        have = Counter(digits)
        for num in range(100, 1000, 2):
            original = num
            d3 = num % 10
            num //= 10
            d2 = num % 10
            num //= 10
            d1 = num % 10
            need = Counter([d1, d2, d3])
            valid = True
            for num, freq in need.items():
                if have[num] < freq:
                    valid = False
                    break
            if valid:
                out.append(original)
        return out


