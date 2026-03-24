# Time to write all of below including tests, explanation and time and aux
# and total space: 6 mins

# Problem: https://leetcode.com/problems/self-dividing-numbers/description/

from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # Time: O(m * log n), m = right - left + 1, n = right
        # Space, excluding output: O(1)
        def check(x: int) -> bool:
            original = x
            while x > 0:
                if x % 10 == 0 or original % (x % 10) != 0:
                    return False
                x //= 10
            return True
        return [num for num in range(left, right + 1) if check(num)]


