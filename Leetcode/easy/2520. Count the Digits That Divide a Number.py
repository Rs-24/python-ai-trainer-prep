# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/

class Solution:
    def countDigits(self, num: int) -> int:
        # Time: O(log num)
        # Space: O(1)
        original = num
        count = 0
        while num > 0:
            d = num % 10
            if d > 0 and original % d == 0:
                count += 1
            num //= 10
        return count


