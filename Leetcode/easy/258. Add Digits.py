# Time to write all of below including tests, explanation and time and aux
# and total space: 9 mins

# Problem: https://leetcode.com/problems/add-digits/description/

class Solution:
    def addDigits(self, num: int) -> int:
        # Time: O(log_10 n), n = num
        # Space: O(1)
        while num > 9:
            total = 0
            while num > 0:
                total += (num % 10)
                num //= 10
            num = total
        return num

# No loop method:
class Solution:
    def addDigits(self, num: int) -> int:
        # Time: O(1)
        # Space: O(1)
        if num == 0:
            return 0
        return 1 + ((num - 1) % 9)


