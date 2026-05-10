# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/smallest-divisible-digit-product-i/description/

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # Time: O((k - n) * log k), k = final answer
        # Space: O(1)
        def check(x: int) -> bool:
            product = 1
            while x > 0:
                product *= x % 10
                x //= 10
            return product % t == 0
        while not check(n):
            n += 1
        return n 


