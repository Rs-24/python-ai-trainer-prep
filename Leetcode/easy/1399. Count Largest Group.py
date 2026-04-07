# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/count-largest-group/description/

class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Time: O(n log n)
        # Space: O(n)
        def get_digit_sum(x: int) -> int:
            total = 0
            while x > 0:
                total += (x % 10)
                x //= 10
            return total
        d = {}
        for i in range(1, n + 1):
            digit_sum = get_digit_sum(i)
            d[digit_sum] = d.get(digit_sum, 0) + 1
        best = max(d.values())
        return sum(1 for s in d.values() if s == best)


