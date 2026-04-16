# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/count-integers-with-even-digit-sum/description/

class Solution:
    def countEven(self, num: int) -> int:
        # Time: O(n log n), n = num
        # Space: O(1)
        def check(x: int) -> bool:
            digit_sum = 0
            while x > 0:
                digit_sum += x % 10
                x //= 10
            return digit_sum % 2 == 0
        count = 0
        for i in range(1, num + 1):
            count += 1 if check(i) else 0
        return count


