

from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: list) -> list:
        # Time: O(1)
        # Space: O(1)
        out = []
        have = Counter(digits)
        for num in range(100, 1000, 2):
            d3 = num % 10
            num //= 10
            d2 = num % 10
            num //= 10
            d1 = num % 10
            need = Counter([d1, d2, d3])
            valid = True
            for d, freq in need.items():
                if freq > have[d]:
                    valid = False
                    break 
            if valid:
                out.append(d1 * 100 + d2 * 10 + d3)
        return out


